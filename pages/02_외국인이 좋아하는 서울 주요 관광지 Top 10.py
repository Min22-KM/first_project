import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(page_title="서울 관광지 지도", layout="wide")

st.title("외국인이 좋아하는 서울 주요 관광지 Top 10 🏙️")

# 관광지 데이터 (설명 확장, 이모지 추가)
tourist_spots = [
    {"name": "경복궁", "lat": 37.579617, "lon": 126.977041, 
     "desc": "🏯 조선 왕조의 대표 궁궐로, 화려한 전통 건축과 궁궐 문화를 체험할 수 있어요. 한국 전통 의상을 입고 사진을 찍기에도 최적의 장소입니다."},
    {"name": "명동", "lat": 37.560966, "lon": 126.986073, 
     "desc": "🛍️ 쇼핑과 길거리 음식의 천국! 다양한 패션 브랜드와 맛있는 길거리 간식을 즐기며 활기찬 서울의 분위기를 느낄 수 있어요."},
    {"name": "남산서울타워", "lat": 37.551169, "lon": 126.988227, 
     "desc": "🌃 서울의 멋진 전경과 야경을 한눈에 볼 수 있는 랜드마크. 연인과 함께 방문하면 사랑의 자물쇠도 걸 수 있어요."},
    {"name": "홍대", "lat": 37.556264, "lon": 126.922648, 
     "desc": "🎨 젊은 예술과 음악의 거리, 독특한 카페와 거리 공연, 벽화가 가득한 힙한 동네입니다."},
    {"name": "인사동", "lat": 37.574361, "lon": 126.984639, 
     "desc": "🖌️ 전통과 현대가 공존하는 문화 거리. 전통 찻집, 공예품, 갤러리 등을 구경하며 한국의 예술과 문화를 체험할 수 있어요."},
    {"name": "동대문디자인플라자(DDP)", "lat": 37.566295, "lon": 127.009151, 
     "desc": "🏢 독특한 현대 건축물과 전시 공간이 매력적입니다. 패션쇼, 디자인 전시 등 다양한 문화 행사가 열려 볼거리가 풍부해요."},
    {"name": "북촌한옥마을", "lat": 37.582604, "lon": 126.983131, 
     "desc": "🏘️ 전통 한옥이 모여 있는 마을로, 옛 서울의 정취를 느낄 수 있어요. 사진 찍기 좋은 명소가 많습니다."},
    {"name": "청계천", "lat": 37.570072, "lon": 126.976934, 
     "desc": "🌊 도심 속 개천을 따라 걷는 산책로. 밤에는 조명이 아름답게 비춰져 로맨틱한 분위기를 즐길 수 있어요."},
    {"name": "광장시장", "lat": 37.570114, "lon": 126.994567, 
     "desc": "🥢 다양한 전통 음식과 간식을 맛볼 수 있는 전통 시장. 빈대떡, 떡볶이, 마약김밥 등 한국 음식 체험에 최적입니다."},
    {"name": "잠실 롯데월드타워", "lat": 37.513943, "lon": 127.102273, 
     "desc": "🏙️ 서울의 초고층 빌딩으로, 전망대에서 서울 전경을 감상할 수 있어요. 쇼핑몰과 아쿠아리움 등 다양한 즐길거리도 있습니다."}
]

# 지도 생성 (서울 중심)
seoul_map = folium.Map(location=[37.5665, 126.9780], zoom_start=12, width="70%", height="70%")

# 마커 추가 (빨강색)
for spot in tourist_spots:
    folium.Marker(
        location=[spot["lat"], spot["lon"]],
        popup=f"{spot['name']} 📍",
        icon=folium.Icon(color="red")
    ).add_to(seoul_map)

# Streamlit에 지도 표시
st_data = st_folium(seoul_map, width=700, height=500)

# 관광지 설명 표시
st.header("관광지 설명 ✨")
for spot in tourist_spots:
    st.subheader(f"{spot['name']} {spot['desc'][:0]}")  # 이름만 강조
    st.write(spot["desc"])

