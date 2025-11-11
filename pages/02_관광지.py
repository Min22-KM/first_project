import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(page_title="Seoul Top10 Attractions", layout="wide")

st.title("🌏 Top 10 Attractions in Seoul (Loved by Foreign Visitors)")
st.write("서울을 처음 방문하는 외국인이 특히 많이 찾는 관광 명소를 지도에 표시했습니다.")

# 주요 관광지 데이터
locations = [
    {"name": "Gyeongbokgung Palace", "lat": 37.579617, "lon": 126.977041, "desc": "한국을 대표하는 궁궐"},
    {"name": "Myeongdong Shopping Street", "lat": 37.560989, "lon": 126.986325, "desc": "외국인 쇼핑 성지"},
    {"name": "N Seoul Tower (Namsan)", "lat": 37.551169, "lon": 126.988227, "desc": "서울의 전망 명소"},
    {"name": "Bukchon Hanok Village", "lat": 37.582671, "lon": 126.983045, "desc": "전통 가옥 거리"},
    {"name": "Hongdae Street", "lat": 37.557192, "lon": 126.924903, "desc": "젊음과 예술의 거리"},
    {"name": "Insadong", "lat": 37.574009, "lon": 126.984849, "desc": "전통문화 체험"},
    {"name": "Dongdaemun Design Plaza (DDP)", "lat": 37.566536, "lon": 127.009879, "desc": "디자인 & 전시"},
    {"name": "COEX & Starfield Library", "lat": 37.513268, "lon": 127.058580, "desc": "별마당 도서관"},
    {"name": "Lotte World Tower", "lat": 37.512466, "lon": 127.102515, "desc": "서울의 랜드마크"},
    {"name": "Hangang Park (Banpo Bridge)", "lat": 37.512370, "lon": 126.995550, "desc": "밤에 예쁜 분수쇼"},
]

# 서울 중심 위치
seoul_center = [37.5665, 126.9780]

# Folium 지도 생성
m = folium.Map(location=seoul_center, zoom_start=12)

# 마커 표시
for place in locations:
    folium.Marker(
        [place["lat"], place["lon"]],
        popup=f"{place['name']} - {place['desc']}",
        tooltip=place["name"],
        icon=folium.Icon(icon="info-sign")
    ).add_to(m)

# Streamlit에 Folium 지도 출력
st_folium(m, width=900, height=600)
