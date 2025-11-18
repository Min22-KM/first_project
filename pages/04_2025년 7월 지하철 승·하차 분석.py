import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="지하철 분석", layout="wide")

st.title("🚇 2025년 7월 지하철 승·하차 분석 대시보드")
st.write("데이터 하나로 세상을 이해하는 중… 😎📊")

# CSV 불러오기 (루트 폴더에 subway.csv가 있다고 가정)
df = pd.read_csv("subway.csv", encoding="cp949")

# 날짜 데이터 정리
df["사용일자"] = df["사용일자"].astype(str)
july_days = sorted(df["사용일자"].unique())

# 날짜 선택
selected_day = st.selectbox("📅 날짜 선택 (2025년 7월)", july_days)

# 호선 선택
lines = sorted(df["노선명"].unique())
selected_line = st.selectbox("🚇 호선 선택", lines)

# 데이터 필터링
filtered = df[(df["사용일자"] == selected_day) &
              (df["노선명"] == selected_line)].copy()

# 총 승객 계산
filtered["총승객"] = filtered["승차총승객수"] + filtered["하차총승객수"]
filtered = filtered.sort_values("총승객", ascending=False)

st.subheader(f"🔥 {selected_day} · {selected_line} 승객 랭킹")

# 색상: 1등 빨강 + 나머지 회색 톤
colors = ["red"] + ["#bfbfbf" for _ in range(len(filtered) - 1)]

# Plotly 그래프
fig = go.Figure(
    data=[
        go.Bar(
            x=filtered["역명"],
            y=filtered["총승객"],
            marker=dict(color=colors)
        )
    ]
)

fig.update_layout(
    title="총 승객수(승차 + 하차) 랭킹 그래프",
    xaxis_title="역명",
    yaxis_title="총 승객수",
    template="simple_white"
)

st.plotly_chart(fig, use_container_width=True)

st.info("1등 역은 레드카펫 깔아드렸습니다 ❤️ 나머지는 잔잔한 회색톤으로 편안하게 정렬!")
