import streamlit as st
from streamlit_folium import st_folium
import folium
from datetime import datetime

st.set_page_config(page_title="서울 관광지 지도", layout="wide")

st.title("외국인이 좋아하는 서울 주요 관광지 Top 10 🏙️")

# 날짜 선택
travel_date = st.date_input("여행 날짜 선택", datetime.today())

# 관광지 데이터 (설명 + 영어 + 가까운 지하철역)
tourist_spots = [
    {"name": "경복궁", "lat": 37.579617, "lon": 126.977041,
     "desc_kr": "🏯 조선 왕조의 대표 궁궐로, 화려한 전통 건축과 궁궐 문화를 체험할 수 있어요. 한국 전통 의상을 입고 사진을 찍기에도 최적의 장소입니다.",
     "desc_en": "Gyeongbokgung Palace is the main palace of the Joseon Dynasty, offering traditional architecture and cultural experiences. It's perfect for photos in traditional Korean clothing.",
     "subway": "3호선 경복궁역"},
    
    {"name": "명동", "lat": 37.560966, "lon": 126.986073,
     "desc_kr": "🛍️ 쇼핑과 길거리 음식의 천국! 다양한 패션 브랜드와 맛있는 길거리 간식을 즐기며 활기찬 서울의 분위기를 느낄 수 있어요.",
     "desc_en": "Myeongdong is a shopping and street food heaven. Enjoy diverse fashion brands and tasty street snacks while experiencing the lively Seoul atmosphere.",
     "subway": "4호선 명동역"},
    
    {"name": "남산서울타워", "lat": 37.551169, "lon": 126.988227,
     "desc_kr": "🌃 서울의 멋진 전경과 야경을 한눈에 볼 수 있는 랜드마크. 연인과 함께 방문하면 사랑의 자물쇠도 걸 수 있어요.",
     "desc_en": "Namsan Seoul Tower offers panoramic views of Seoul. Couples can also hang 'love locks' while enjoying the city lights.",
     "subway": "4호선 명동역"},
    
    {"name": "홍대", "lat": 37.556264, "lon": 126.922648,
     "desc_kr": "🎨 젊은 예술과 음악의 거리, 독특한 카페와 거리 공연, 벽화가 가득한 힙한 동네입니다.",
     "desc_en": "Hongdae is a vibrant district full of young art, music, unique cafes, street performances, and murals.",
     "subway": "2호선 홍대입구역"},
    
    {"name": "인사동", "lat": 37.574361, "lon": 126.984639,
     "desc_kr": "🖌️ 전통과 현대가 공존하는 문화 거리. 전통 찻집, 공예품, 갤러리 등을 구경하며 한국의 예술과 문화를 체험할 수 있어요.",
     "desc_en": "Insadong is a cultural street where tradition meets modernity. Explore tea houses, crafts, and galleries to experience Korean arts and culture.",
     "subway": "1호선 종로3가역"},
    
    {"name": "동대문디자인플라자(DDP)", "lat": 37.566295, "lon": 127.009151,
     "desc_kr": "🏢 독특한 현대 건축물과 전시 공간이 매력적입니다. 패션쇼, 디자인 전시 등 다양한 문화 행사가 열려 볼거리가 풍부해요.",
     "desc_en": "Dongdaemun Design Plaza features unique modern architecture and exhibition spaces. Fashion shows and design exhibitions offer plenty to see.",
     "subway": "2호선 동대문역"},
    
    {"name": "북촌한옥마을", "lat": 37.582604, "lon": 126.983131,
     "desc_kr": "🏘️ 전통 한옥이 모여 있는 마을로, 옛 서울의 정취를 느낄 수 있어요. 사진 찍기 좋은 명소가 많습니다.",
     "desc_en": "Bukchon Hanok Village is a traditional village where visitors can feel the old Seoul atmosphere. Many spots are perfect for photography.",
     "subway": "3호선 안국역"},
    
    {"name": "청계천", "lat": 37.570072, "lon": 126.976934,
     "desc_kr": "🌊 도심 속 개천을 따라 걷는 산책로. 밤에는 조명이 아름답게 비춰져 로맨틱한 분위기를 즐길 수 있어요.",
     "desc_en": "Cheonggyecheon is a stream-side walking path in the city. At night, lights create a romantic atmosphere.",
     "subway": "1호선 종각역"},
    
    {"name": "광장시장", "lat": 37.570114, "lon": 126.994567,
     "desc_kr": "🥢 다양한 전통 음식과 간식을 맛볼 수 있는 전통 시장. 빈대떡, 떡볶이, 마약김밥 등 한국 음식 체험에 최적입니다.",
     "desc_en": "Gwangjang Market is a traditional market where you can taste various Korean foods like bindaetteok, tteokbokki, and gimbap.",
     "subway": "1호선 종로5가역"},
    
    {"name": "잠실 롯데월드타워", "lat": 37.513943, "lon": 127.102273,
     "desc_kr": "🏙️ 서울의 초고층 빌딩으로, 전망대에서 서울 전경을 감상할 수 있어요. 쇼핑몰과 아쿠아리움 등 다양한 즐길거리도 있습니다.",
     "desc_en": "Lotte World Tower is a super-tall building offering panoramic views from its observation deck. Shopping and an aquarium provide fun activities.",
     "subway": "2호선 잠실역"}
]

# 지도 생성
seoul_map = folium.Map(location=[37.5665, 126.9780], zoom_start=12, width="70%", height="70%")

# 마커 추가
for spot in tourist_spots:
    folium.Marker(
        location=[spot["lat"], spot["lon"]],
        popup=f"{spot['name']} 📍\nSubway: {spot['subway']}",
        icon=folium.Icon(color="red")
    ).add_to(seoul_map)

# 지도 표시
st_data = st_folium(seoul_map, width=700, height=500)

# 관광지 설명 표시
st.header("관광지 설명 ✨")
for spot in tourist_spots:
    st.subheader(f"{spot['name']} ({spot['subway']})")
    st.write(spot["desc_kr"])
    st.write(spot["desc_en"])

# 선택한 날짜 기준 일정 요약
st.header("여행 일정 🗓️")
st.write(f"📅 {travel_date.strftime('%Y년 %m월 %d일')} 일정:")
for i, spot in enumerate(tourist_spots, start=1):
    st.write(f"{i}. {spot['name']} ({spot['subway']})")
