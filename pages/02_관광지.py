import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="서울 관광지 지도", layout="wide")

st.title("외국인이 좋아하는 서울 주요 관광지 Top 10")

# 관광지 데이터
tourist_spots = [
    {"name": "경복궁", "lat": 37.579617, "lon": 126.977041, "desc": "조선 왕조의 대표 궁궐, 전통 건축 감상 가능"},
    {"name": "명동", "lat": 37.560966, "lon": 126.986073, "desc": "쇼핑과 길거리 음식으로 유명한 서울 중심 상업지구"},
    {"name": "남산서울타워", "lat": 37.551169, "lon": 126.988227, "desc": "서울 전망과 야경을 즐길 수 있는 랜드마크"},
    {"name": "홍대", "lat": 37.556264, "lon": 126.922648, "desc": "예술과 음악, 젊은 감성이 넘치는 핫플레이스"},
    {"name": "인사동", "lat": 37.574361, "lon": 126.984639, "desc": "전통문화와 예술, 공예품 거리"},
    {"name": "동대문디자인플라자(DDP)", "lat": 37.566295, "lon": 127.009151, "desc": "독특한 현대 건축과 전시, 패션의 중심지"},
    {"name": "북촌한옥마을", "lat": 37.582604, "lon": 126.983131, "desc": "전통 한옥 마을, 사진 촬영 명소"},
    {"name": "청계천", "lat": 37.570072, "lon": 126.976934, "desc": "도심 속 개천 산책, 야경과 휴식 공간"},
    {"name": "광장시장", "lat": 37.570114, "lon": 126.994567, "desc": "전통 시장, 한국 음식 체험 가능"},
    {"name": "잠실 롯데월드타워", "lat": 37.513943, "lon": 127.102273, "desc": "서울의 초고층 빌딩, 전망대와 쇼핑몰"}
]

# 지도 생성 (서울 중심)
seoul_map = folium.Map(location=[37.5665, 126.9780], zoom_start=12, width="70%", height="70%")

# 마커 추가
for spot in tourist_spots:
    folium.Marker(
        location=[spot["lat"], spot["lon"]],
        popup=spot["name"],
        icon=folium.Icon(color="red")
    ).add_to(seoul_map)

# Streamlit에 지도 표시
st_data = st_folium(seoul_map, width=700, height=500)

# 관광지 설명 표시
st.header("관광지 설명")
for spot in tourist_spots:
    st.subheader(spot["name"])
    st.write(spot["desc"])
