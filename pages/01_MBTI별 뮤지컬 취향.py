import streamlit as st
import random

st.title("🎭 MBTI별 뮤지컬 추천기")
st.write("너의 MBTI에 맞는 뮤지컬을 추천해줄게! ✨")

mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

choice = st.selectbox("너의 MBTI를 골라봐~ 🧾", mbti_list, key="mbti_select")

# MBTI별 추천 뮤지컬 데이터
musical_recommendations = {
    "INTJ": {
        "korean": [
            ("마리 퀴리", "이성과 신념이 충돌하는 과학자의 고뇌가 돋보여요."),
            ("베르테르", "집요한 감정선과 내면의 고독이 INTJ에게 깊이 와닿아요.")
        ],
        "global": [
            ("레미제라블", "사상과 정의의 싸움, INTJ의 도덕적 통찰력과 닮았어요."),
            ("지킬 앤 하이드", "이중성과 자기 통제의 상징, 논리와 광기의 경계죠.")
        ]
    },
    "INFP": {
        "korean": [
            ("레드북", "이상과 자유를 꿈꾸는 감성파 INFP에게 찰떡이에요."),
            ("광화문 연가", "그리움과 순수한 사랑의 향기가 가득한 작품이에요.")
        ],
        "global": [
            ("디어 에반 핸슨", "내면의 불안과 공감의 서사가 INFP 마음을 울려요."),
            ("스프링 어웨이크닝", "청춘의 이상과 현실의 충돌, INFP 감성에 찰떡!")
        ]
    },
    "ENFP": {
        "korean": [
            ("모래시계", "열정과 정의감이 넘치는 서사에 ENFP의 불꽃이 느껴져요."),
            ("번지점프를 하다", "운명적인 사랑에 끌리는 낭만파 ENFP에게 딱이에요.")
        ],
        "global": [
            ("헤어스프레이", "긍정 에너지와 사회변화의 메시지가 ENFP에 어울려요."),
            ("맘마미아!", "자유롭고 즉흥적인 모험심에 딱 맞는 뮤지컬이에요.")
        ]
    },
    "ISTJ": {
        "korean": [
            ("영웅", "충직하고 신념 있는 영웅의 서사가 ISTJ에게 어울려요."),
            ("팬레터", "논리적이지만 내면에 감성이 깃든 ISTJ를 표현해요.")
        ],
        "global": [
            ("오페라의 유령", "헌신과 완벽주의, ISTJ의 섬세한 몰입력과 닮았어요."),
            ("레미제라블", "원칙과 정의에 충실한 인물들이 매력적이에요.")
        ]
    },
    "ISFP": {
        "korean": [
            ("웃는 남자", "비극 속에서도 예술을 사랑하는 순수한 감성이 돋보여요."),
            ("그날들", "감정의 결을 따라 흐르는 섬세한 감성이 ISFP와 닮았어요.")
        ],
        "global": [
            ("빌리 엘리어트", "자신의 길을 찾아가는 따뜻한 이야기예요."),
            ("웨스트 사이드 스토리", "사랑과 갈등, 예술적 감성이 어우러진 고전이에요.")
        ]
    },
    "ENTJ": {
        "korean": [
            ("마타하리", "리더십과 결단력의 상징, ENTJ의 강렬한 매력과 어울려요."),
            ("시라노", "야망과 이상을 동시에 품은 캐릭터에 공감할 거예요.")
        ],
        "global": [
            ("위키드", "불가능을 현실로 만드는 주인공의 야망이 ENTJ답죠."),
            ("시카고", "전략적이고 카리스마 넘치는 스타일이 ENTJ스러워요.")
        ]
    },
    "INFJ": {
        "korean": [
            ("팬레터", "예술과 이상에 헌신하는 INFJ의 섬세한 내면을 담았어요."),
            ("마리 퀴리", "신념과 윤리의 갈등, INFJ의 철학적 고민을 닮았죠.")
        ],
        "global": [
            ("디어 에반 핸슨", "타인을 이해하고 위로하려는 INFJ의 따뜻함이 보여요."),
            ("넥스트 투 노멀", "가족과 감정의 깊은 관계를 탐구하는 작품이에요.")
        ]
    },
    "ESFP": {
        "korean": [
            ("젊음의 행진", "흥과 에너지로 가득한 무대, ESFP의 무대감각에 딱이에요."),
            ("광화문 연가", "감성적이고 낭만적인 ESFP의 감정선을 자극하죠.")
        ],
        "global": [
            ("맘마미아!", "파티와 음악, 인생을 즐기는 ESFP의 세계예요."),
            ("위키드", "화려하고 드라마틱한 전개가 ESFP의 감정선을 사로잡아요.")
        ]
    }
}

# MBTI 유형에 대한 스타일 예측
style_predictions = {
    "INTJ": "🧠 분석하면서 몰입하는 타입! 무대 연출에 집중할 확률 높아요.",
    "INFP": "🎨 감정이입 만렙! 눈물 한 방울 예상돼요.",
    "ENFP": "🌈 친구랑 떠들며 감정 폭발형 관객!",
    "ISTJ": "📋 팜플렛 꼼꼼히 보고 질서 있게 관극하는 스타일.",
    "ISFP": "🍃 조용히 감상하지만 속으로 감정이 파도처럼 이는 스타일.",
    "ENTJ": "🔥 연출·기획 포인트를 분석하며 보는 전략형 관객.",
    "INFJ": "🌙 인물의 내면에 깊이 공감하며 몰입하는 감성파.",
    "ESFP": "🎉 신나는 넘버에 몸이 들썩! 현실형 즐김러."
}

# 버튼 구성
show_korean = st.button("🇰🇷 국내 창작뮤지컬만 보기", key="korean_only")
show_all = st.button("🌍 전체 추천 보기", key="all_musical")

# 추천 로직
if choice:
    st.subheader(f"💡 {choice}에게 어울리는 뮤지컬은?")
    data = musical_recommendations.get(choice, {})

    if show_korean:
        for title, comment in data.get("korean", []):
            st.write(f"🎵 **{title}** — {comment}")
        st.write("좋은 음악과 연출로 즐거운 관람이 될 거예요! 🎶")

    elif show_all or not show_korean:
        for title, comment in data.get("korean", []):
            st.write(f"🎵 **{title}** — {comment}")
        for title, comment in data.get("global", []):
            st.write(f"🌍 **{title}** — {comment}")
        st.write("좋은 음악과 연출로 즐거운 관람이 될 거예요! 🎶")

    st.markdown(f"---\n**{style_predictions.get(choice, '')}**")
