import streamlit as st

# 타이틀에 작은따옴표가 포함되어 있어 큰따옴표로 감쌌음
st.title("MinYi's first project!")

# 입력창
a = st.text_input('안녕! 난 유미야! 만나서 반가워!')
b = st.selectbox('혹시 좋아하는 e스포츠 팀 있어?', ['티원', 'T1', '젠지', '한화'])

# 버튼 누르면 인사 메시지 출력
if st.button('인사말 생성'):
    # 사용자 입력이 비어있을 때의 안전 처리 추가 (빈 문자열이면 기본 문구)
    name = a.strip() if a and a.strip() else '유미'
    team = b

    st.info(f'{name} 너랑 딱 붙어있을게! 냥~ 냥! 😺')
    st.warning(f'{team}를 좋아하는구나! 나도 그거 좋아해! 👍')
    st.error('너한테 머릴 비비는 건, 널 찜했다는 뜻이야. 💘')
    st.balloons()
