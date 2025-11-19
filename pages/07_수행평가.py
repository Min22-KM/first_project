import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="예술의전당 장르 분석", layout="wide")

st.title("🎭 예술의전당 공연/전시 장르 분석 🖼️")
st.write("연도를 선택하면 그 해에 제일 인기 많았던 장르를 보여줍니다. 😎")

# CSV 파일 불러오기
df = pd.read_csv("예술의전당_공연 및 전시 안내_20250514.csv")

# '연도' 컬럼 만들기 (공연 시작일 기준)
if '공연시작일' in df.columns:
    df['연도'] = pd.to_datetime(df['공연시작일'], errors='coerce').dt.year
else:
    st.error("공연 시작일 컬럼이 없어요 ㅠㅠ 파일 확인해 주세요!")
    st.stop()

# 연도 선택
years = sorted(df['연도'].dropna().unique())
selected_year = st.selectbox("🔹 연도를 선택해 주세요", years)

# 선택한 연도 데이터 필터링
year_data = df[df['연도'] == selected_year]

if '장르' not in year_data.columns:
    st.error("장르 컬럼이 없네요! 파일 구조 확인 필수 🔍")
    st.stop()

# 장르별 공연 수 집계
genre_count = year_data['장르'].value_counts().reset_index()
genre_count.columns = ['장르', '횟수']

# 색상 그라데이션: 1등부터 연해지는 블루
max_count = genre_count['횟수'].max()
colors = [f'rgba(0,0,255,{0.3 + 0.7*(count/max_count)})' for count in genre_count['횟수']]

# Plotly 막대그래프
fig = px.bar(
    genre_count,
    x='장르',
    y='횟수',
    text='횟수',
    color='횟수',
    color_continuous_scale=px.colors.sequential.Blues_r,  # 1등부터 연해지는 파랑
)

fig.update_traces(textposition='outside')
fig.update_layout(
    title=f"✨ {selected_year}년 가장 많이 공연된 장르 TOP 🏆",
    xaxis_title="장르",
    yaxis_title="공연 수",
    coloraxis_showscale=False,
)

st.plotly_chart(fig, use_container_width=True)

st.write("💡 청소년 여러분, 이 해에는 어떤 장르가 유행했는지 눈치챘나요? 😎👀")
