import streamlit as st
import random

st.set_page_config(page_title="MBTI → 뮤지컬 추천소", page_icon="🎭", layout="centered")

st.title("MBTI별 뮤지컬 추천소 🎭✨")
st.caption("하나 골라서 너에게 찰떡인 뮤지컬 2편과 관극 스타일을 알려줄게! (추가 설치 불필요) ")

mbti_list = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ",
]

# MBTI -> (추천 뮤지컬 2개, 관극 스타일 설명)
MBTI_MAP = {
    "ISTJ": ("마이 페어 레이디, 오페라의 유령",
             "차분히 앉아 배우 디테일을 챙기는 타입. 줄거리·연출에 집중하며 박수 타이밍을 놓치지 않음 👌"),
    "ISFJ": ("사운드 오브 뮤직, 라이온 킹",
             "감성 충만 힐링 모드. 배우 표정에 공감하면서 살짝 눈물 글썽일 수 있음 😌💐"),
    "INFJ": ("레 미제라블, 디어 에반 핸슨",
             "스토리와 메시지에 깊게 몰입. 공연 끝나고 생각 정리하느라 한동안 말수가 적어짐 🧠💭"),
    "INTJ": ("해밀턴, 스위니 토드",
             "연출 의도와 구조 해석을 좋아함. 상징을 찾아내며 뿌듯해함 🕵️‍♂️📘"),
    "ISTP": ("시카고, 위키드",
             "무대 기술·안무 보는 재미! 웃음 포인트를 놓치지 않음 😎🎬"),
    "ISFP": ("호프: 읽히지 않은 책과 읽히지 않은 삶, 문스토리",
             "감성 & 비주얼에 취함. 포스터 하나에도 감동하는 타입 🎨📸"),
    "INFP": ("베르테르, 렌트",
             "감성! 감성!! 감성!!! 노래 한 소절에 심장이 녹음 💕"),
    "INTP": ("난설, 스프링 어웨이크닝",
             "연출적 장치를 관찰하며 머릿속에서 퍼즐 맞추는 타입 📝🤓"),
    "ESTP": ("그리스, 젠틀맨스 가이드",
             "분위기 타는 흥폭발형. 리듬 들리면 이미 춤추고 있음 🕺🔥"),
    "ESFP": ("맘마미아!, 캣츠",
             "공연=파티! 배우와 눈 마주치면 반응 폭발 🥳🎉"),
    "ENFP": ("웃는 남자, 광화문 연가",
             "공연 보고 갑자기 인생에 대해 토론하고 싶어짐 ✨🖍️"),
    "ENTP": ("프로듀서스, 아마데우스(연극+뮤지컬 연출 변형)",
             "풍자·유머 포착 천재. 가장 크게 웃는 사람 😏🎭"),
    "ESTJ": ("웨스트 사이드 스토리, 시카고",
             "정확한 박수 타이밍, 좌석도 미리 전략적으로 예매 ✅👏"),
    "ESFJ": ("디어 에반 핸슨, 서편제",
             "같이 보는 사람 챙기며 감정 공유하는 타입 💕🎫"),
    "ENFJ": ("레 미제라블, 엑스칼리버",
             "스토리 메시지 중요. 주변 사람들 감동시키는 사람 🌟🤝"),
    "ENTJ": ("스위니 토드, 드라큘라",
             "큰 그림 보고 작품 분석. 전략적 관극가 🧭🏆"),
}

st.write("---")

def display_recommendation(mbti):
    musicals, style = MBTI_MAP.get(mbti, ("—","—"))
    mus_list = [m.strip() for m in musicals.split(",")]

    st.subheader(f"{mbti}님에게 추천하는 뮤지컬 2선 🎯")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**1. {mus_list[0]}**")
        # 가벼운 추천 이유 (짧게)
        st.write(get_short_reason(mus_list[0], mbti))
    with col2:
        st.markdown(f"**2. {mus_list[1]}**")
        st.write(get_short_reason(mus_list[1], mbti))

    st.markdown("---")
    st.markdown("### 관극 예상 스타일 — 리얼리티 버전 🎬")
    st.write(style)

    # 재방문/공감 버튼
    if st.button("비슷한 유형 더 보기 / 랜덤 추천 🎲"):
        other = random.choice([m for m in mbti_list if m != mbti])
        st.info(f"비슷한 유형: **{other}** — 한 번 보고 느껴봐! 👀")


def get_short_reason(musical, mbti):
    # 간단한 뮤지컬별 이유(청소년 친근한 느낌)
    reasons = {
        "My Fair Lady": "클래식한 멜로디와 우아한 연출로 안정감을 줘요.",
        "The Phantom of the Opera": "미스터리+로맨스의 조합, 분위기 미쳤음. 분위기용 추천 🎭",
        "Les Misérables": "드라마틱한 대서사, 인생곡 줄줄 나옴. 눈물 주의!",
        "Hamilton": "랩+역사 스토리의 신선한 조합. 듣다 보면 빠져들어용",
        "Wicked": "판타지와 여성 서사가 잘 어울림. 시각적으로 짱!",
        "Moulin Rouge! (musical)": "팝송 믹스와 폭발적 무대 에너지 — 눈이 즐거움",
        "Rent": "청춘의 열정과 현실을 노래하는 작품. 마음이 흔들려요",
        "Once": "소박한 감정선을 담백하게 그려요. 잔잔한 여운~",
        "The Curious Incident of the Dog in the Night-Time": "독특한 시점 연출이 인상적. 뇌가 즐거움",
        "Spring Awakening": "강렬한 청춘 성장물, 에너지 뿜뿜",
        "Chicago": "세련된 재즈 무대와 블랙 유머가 매력",
        "Kinky Boots": "희망과 웃음, 패션 요소까지 즐길 수 있음",
        "Grease": "복고 댄스와 캐치한 넘버로 신나게 즐김",
        "Rock of Ages": "락 뮤지컬의 정수, 흥 넘치는 밤",
        "Mamma Mia!": "팝송과 유쾌한 스토리, 같이 따라부르기 좋아요",
        "Cats": "독특한 퍼포먼스와 곡으로 기억에 오래 남음",
        "Dear Evan Hansen": "내면의 외로움에 공감하게 만드는 작품",
        "Sweeney Todd": "어둡고 강렬한 블랙뮤지컬. 임팩트 강함",
        "The Sound of Music": "가족적이고 따뜻한 스토리로 힐링",
        "The Lion King": "무대미술·의상 예술성 최고, 눈호강",
        "The Book of Mormon": "빵빵 터지는 블랙코미디 스타일",
        "The Producers": "광기 어린 코미디로 관객을 빵 터뜨림",
    }
    return reasons.get(musical, "좋은 음악과 연출로 즐거운 관람이 될 거예요!")

# 인터페이스
st.write("원하는 MBTI를 선택하면 추천과 관극스타일을 알려줘요.")
choice = st.selectbox("너의 MBTI를 골라봐~ 🧾", mbti_list)

if st.button("추천 받을래요 🎟️"):
    display_recommendation(choice)
    st.balloons()

st.write("---")
st.caption("제작: MBTI→뮤지컬 추천기 · 청소년 친화적 멘트 포함. 문의는 댓글로~ 😄")
