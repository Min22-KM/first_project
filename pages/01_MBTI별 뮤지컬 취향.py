import streamlit as st

st.set_page_config(
    page_title="MBTI 뮤지컬 추천 🎭",
    layout="centered"
)

st.title("🎭 MBTI 기반 뮤지컬 추천기")
st.write("뮤지컬 보는 성격 테스트는 아니고… 그냥 네 취향 맞추는 앱임 ㅋㅋ")

mbti_list = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ"
]

recommendations = {
    "ISTJ": {
        "korean": ["영웅", "웃는 남자"],
        "global": ["레 미제라블", "팬텀"]
    },
    "ISFJ": {
        "korean": ["레드북", "서편제"],
        "global": ["맘마미아!", "빌리 엘리어트"]
    },
    "INFJ": {
        "korean": ["마리 퀴리", "프리다"],
        "global": ["데어 오브 에반 한센", "노트르담 드 파리"]
    },
    "INTJ": {
        "korean": ["삼총사", "베르나르다 알바"],
        "global": ["지킬 앤 하이드", "스위니 토드"]
    },
    "ISTP": {
        "korean": ["빈센트 반 고흐", "팬레터"],
        "global": ["시카고", "킹키부츠"]
    },
    "ISFP": {
        "korean": ["광염소나타", "루드윅"],
        "global": ["위키드", "라이온킹"]
    },
    "INFP": {
        "korean": ["너를 위한 글자", "베어 더 뮤지컬"],
        "global": ["스프링 어웨이크닝", "렌트"]
    },
    "INTP": {
        "korean": ["은하철도 999", "더데빌"],
        "global": ["해밀턴", "컴프롬어웨이"]
    },
    "ESTP": {
        "korean": ["곤 투모로우", "오디너리 데이즈"],
        "global": ["록키 호러 쇼", "헤어스프레이"]
    },
    "ESFP": {
        "korean": ["광화문연가", "위대한 캣츠비"],
        "global": ["알라딘", "지저스 크라이스트 수퍼스타"]
    },
    "ENFP": {
        "korean": ["난쟁이들", "셜록홈즈"],
        "global": ["웨스트 사이드 스토리", "맘마미아!"]
    },
    "ENTP": {
        "korean": ["엑스칼리버", "이블데드"],
        "global": ["북 오브 모몬", "지킬 앤 하이드"]
    },
    "ESTJ": {
        "korean": ["지킬 앤 하이드(창작/라이선스 혼재)", "영웅"],
        "global": ["오페라의 유령", "레미제라블"]
    },
    "ESFJ": {
        "korean": ["김종욱 찾기", "라흐 헤스트"],
        "global": ["드림걸즈", "애니"]
    },
    "ENFJ": {
        "korean": ["웃는 남자", "프랑켄슈타인"],
        "global": ["렌트", "레미제라블"]
    },
    "ENTJ": {
        "korean": ["마타하리", "더데빌"],
        "global": ["해밀턴", "캐치 미 이프 유 캔"]
    }
}

choice = st.selectbox("너의 MBTI를 골라봐~ 🧾", mbti_list, key="mbti_select")

st.write("---")

if choice:
    st.subheader(f"✨ {choice} 유형에게 추천하는 뮤지컬 ✨")

    korean = recommendations[choice]["korean"]
    global_ = recommendations[choice]["global"]

    st.write("🇰🇷 **국내 창작 & 국내 공연**")
    st.write(f"- {korean[0]}")
    st.write(f"- {korean[1]}")

    st.write("🌎 **해외 뮤지컬 (라이선스 공연 포함)**")
    st.write(f"- {global_[0]}")
    st.write(f"- {global_[1]}")

    st.success("좋은 음악과 연출로 즐거운 관람이 될 거예요! 🎶")

    if st.button("국내 창작뮤지컬만 보기 🎫", key="korean_only_button"):
        st.write("🇰🇷 **국내 창작뮤지컬만 보기**")
        st.write(f"- {korean[0]}")
        st.write(f"- {korean[1]}")
        st.success("좋은 음악과 연출로 즐거운 관람이 될 거예요! 🎶")
