import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="지하철 분석", layout="wide")

st.title("🚇 2025년 7월 지하철 승·하차 분석 대시보드")
st.write("데이터 하나로 도시의 흐름을 읽어보자… 😎📊")

# CSV 불러오기
df = pd.read_csv("subway.csv", encoding="cp949")

# 날짜 처리
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

filtered["총승객"] = filtered["승차총승객수"] + filtered["하차총승객수"]
filtered = filtered.sort_values("총승객", ascending=False)

st.subheader(f"🔥 {selected_day} · {selected_line} 승객 랭킹")

# 1등은 빨강, 나머지는 회색
colors = ["red"] + ["#bfbfbf" for _ in range(len(filtered) - 1)]

# 그래프 표시
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
    title="총 승객수(승차 + 하차) 랭킹",
    xaxis_title="역명",
    yaxis_title="총 승객수",
    template="simple_white"
)

st.plotly_chart(fig, use_container_width=True)


# ------------------------------------------
# 🚨 추가 기능: 선택한 호선에서 가장 규모가 큰 역 분석
# ------------------------------------------

top_station = filtered.iloc[0]  # 총승객 기준 1위

st.subheader("⚡ 선택한 호선에서 가장 규모가 큰 역 분석")

st.success(
    f"### 🏆 {selected_line} 대표 역은 **{top_station['역명']}역**입니다!\n"
    f"- 📊 총승객수: **{top_station['총승객']:,}명**\n"
    f"- 🚉 승차: **{top_station['승차총승객수']:,}명**\n"
    f"- 🛬 하차: **{top_station['하차총승객수']:,}명**\n\n"
    f"이 역은 같은 호선 내에서 **절대 강자급 규모**를 보여주는 역이에요. "
    f"사람 흐름이 가장 두꺼운 지점이라는 뜻이죠 😎🔥"
)

st.info("호선 전체에서 ‘규모 1등 역’을 자동으로 분석해 보여주는 기능이에요!")
