import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="예술의전당 장르 분석", layout="wide")

st.title("🎭 예술의전당 장르 분석기 🎶")
st.write("연도 고르면 그 해 어떤 장르가 제일 핫했는지 바로 알려주는 앱입니다 😎🔥")

# -------------------------------------------------
# CSV 불러오기 (인코딩 오류 해결)
# -------------------------------------------------
try:
    df = pd.read_csv("예술의전당_공연 및 전시 안내_20250514.csv", encoding="cp949")
except UnicodeDecodeError:
    df = pd.read_csv("예술의전당_공연 및 전시 안내_20250514.csv", encoding="utf-8-sig")

# -------------------------------------------------
# 날짜 → 연도 추출
# -------------------------------------------------
if "공연시작일" not in df.columns:
    st.error("❗ '공연시작일' 컬럼이 없어요. CSV 구조를 확인해주세요!")
    st.stop()

df["연도"] = pd.to_datetime(df["공연시작일"], errors="coerce").dt.year
years = sorted(df["연도"].dropna().unique())

selected_year = st.selectbox("📅 분석할 연도 선택", years)

# -------------------------------------------------
# 선택한 연도의 데이터 필터링
# -------------------------------------------------
year_df = df[df["연도"] == selected_year]

if "장르" not in year_df.columns:
    st.error("❗ '장르' 컬럼이 없어요. 파일 구조를 반드시 확인해야 합니다!")
    st.stop()

genre_count = year_df["장르"].value_counts().reset_index()
genre_count.columns = ["장르", "횟수"]

# -------------------------------------------------
# Plotly 색상: 1등 → 진한 파랑, 아래로 갈수록 연해지는 Blue Gradient
# -------------------------------------------------
fig = px.bar(
    genre_count,
    x="장르",
    y="횟수",
    text="횟수",
    color="횟수",
    color_continuous_scale=px.colors.sequential.Blues,
)

fig.update_traces(textposition="outside")
fig.update_layout(
    title=f"✨ {selected_year}년 가장 많이 공연된 장르 TOP 🎤",
    xaxis_title="장르",
    yaxis_title="공연 수",
    coloraxis_showscale=False,
)

st.plotly_chart(fig, use_container_width=True)

st.write(
    f"📌 {selected_year}년에 이런 장르들이 🔥인기 폭발🔥 했네요!  
    요즘 감성으로 보면… ‘이 정도면 흥행 보장이지 않나요? 😎’"
)

