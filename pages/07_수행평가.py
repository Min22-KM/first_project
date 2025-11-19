"""
t1_match_scraper.py
- 목적: op.gg + 네이버 e스포츠를 메인 소스로 사용하여 T1의 경기 기록을 수집하고,
  월별/리그별 승률과 국내팀 상대전적을 계산하여 CSV 파일로 저장합니다.
- 출력:
    ./monthly_winrate.csv
    ./league_winrate.csv
    ./head2head_domestic.csv
- 필요 패키지: requests, beautifulsoup4, pandas, tqdm, selenium (optional)
- 사용법:
    pip install requests beautifulsoup4 pandas tqdm selenium webdriver-manager
    python t1_match_scraper.py
- 실행 결과: 스크립트 실행 폴더에 CSV가 생성됩니다.
"""

import re
import time
import json
from datetime import datetime
from collections import defaultdict
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# Selenium fallback for JS-rendered pages
USE_SELENIUM_FALLBACK = True
try:
    if USE_SELENIUM_FALLBACK:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from webdriver_manager.chrome import ChromeDriverManager
        SELENIUM_OK = True
    else:
        SELENIUM_OK = False
except Exception:
    SELENIUM_OK = False

# --- 설정: 크롤링 대상(수정 가능) ---
OPGG_TEAM_URL = "https://esports.op.gg/teams/385/t1"  # OP.GG T1 팀 페이지
NAVER_ESPORTS_BASE = "https://game.naver.com/esports/League_of_Legends"  # 네이버 e스포츠 LoL 홈

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36"
}

# --- 유틸: selenium 렌더링 함수 ---
def render_url_with_selenium(url, wait_seconds=1.0):
    if not SELENIUM_OK:
        raise RuntimeError("Selenium not available; install selenium and webdriver-manager or disable fallback.")
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    try:
        driver.get(url)
        time.sleep(wait_seconds)
        html = driver.page_source
    finally:
        driver.quit()
    return html

# --- 1) OP.GG에서 가능한 한 경기 목록 수집 ---
def scrape_opgg_team_matches(year=None, max_pages=6):
    """
    시도 순서:
      1) requests로 team page에서 'match list' 블록을 바로 파싱 시도
      2) 결과가 불충분하면 Selenium으로 렌더링해서 다시 파싱
    반환: list of dict {date, opponent, result, league, score, url_source}
    """
    results = []

    # OP.GG 팀 페이지 (기본)
    html = None
    try:
        r = requests.get(OPGG_TEAM_URL, headers=HEADERS, timeout=12)
        if r.status_code == 200 and len(r.text) > 2000:
            html = r.text
    except Exception:
        html = None

    # fallback
    if (not html or "Match schedules" not in html) and SELENIUM_OK:
        try:
            html = render_url_with_selenium(OPGG_TEAM_URL, wait_seconds=1.2)
        except Exception:
            pass

    if not html:
        raise RuntimeError("OP.GG 페이지를 가져오지 못했습니다. 네트워크 또는 Selenium 설치를 확인하세요.")

    soup = BeautifulSoup(html, "html.parser")

    # OP.GG 페이지의 구조는 바뀔 수 있으므로 안전하게 'matches' 링크/블록을 찾는 시도
    # 1) matches 블록을 찾고, 개별 match 엔트리 파싱
    match_blocks = soup.select("div.matches, ul.matches, .match-list, .match_result")
    # fallback find by 'matches' keyword
    if not match_blocks:
        match_blocks = soup.find_all(string=re.compile("Match result|경기 결과|Match schedules|match result", re.I))

    # heuristic parse: 페이지 내의 <a href="/matches/XXXXX"> 링크를 찾아서 개별 match 페이지로 접근
    match_links = set()
    for a in soup.select("a"):
        href = a.get("href") or ""
        if "/matches/" in href and href.count("/")>=2:
            # full or relative
            full = href if href.startswith("http") else "https://esports.op.gg" + href
            match_links.add(full)
    match_links = sorted(match_links)

    # Limit pages to avoid excessive crawling
    if len(match_links) == 0:
        # alternative: league schedule pages (LCK, Worlds...)에서 T1 관련 매치 찾기
        # as fallback, try searching for 'matches' via op.gg schedule pages (short)
        pass

    # fetch and parse each match detail page (더 정확한 결과 획득)
    for link in tqdm(match_links[:max_pages], desc="OP.GG matches"):
        try:
            txt = None
            try:
                r = requests.get(link, headers=HEADERS, timeout=10)
                if r.status_code == 200:
                    txt = r.text
            except Exception:
                txt = None
            if (not txt or len(txt)<200) and SELENIUM_OK:
                txt = render_url_with_selenium(link, wait_seconds=0.8)
            if not txt:
                continue
            s = BeautifulSoup(txt, "html.parser")
            # 날짜 찾기
            date_text = s.find(string=re.compile(r"\d{4}\.\d{2}\.\d{2}|\w+\s+\d{1,2},\s*\d{4}", re.I))
            date_obj = None
            if date_text:
                # try yyyy.mm.dd
                m = re.search(r"(\d{4})\.(\d{2})\.(\d{2})", date_text)
                if m:
                    date_obj = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                else:
                    try:
                        date_obj = datetime.fromisoformat(date_text.strip())
                    except Exception:
                        date_obj = None
            # league
            league = None
            league_tag = s.select_one(".league, .match-league, .league-name")
            if league_tag:
                league = league_tag.get_text(strip=True)
            # teams & score & result
            # look for team blocks
            team_blocks = s.select(".team")
            # fallback by regex
            text = s.get_text(" ", strip=True)
            # try to determine opponent and winner by simple p

