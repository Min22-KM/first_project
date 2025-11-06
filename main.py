import streamlit as st

st.title("MinYi's first project!")

a = st.text_input('안녕! 난 유미야! 만나서 반가워!')
b = st.selectbox('혹시 좋아하는 e스포츠 팀 있어?', ['티원', 'T1', '젠지', '한화'])

if st.button('인사말 생성'):
    st.info(a + ' 너랑 딱 붙어있을게! 냥~ 냥!')
    st.warning(b + '를 좋아하는구나! 나도 그거 좋아해!')
    st.error('너한테 머릴 비비는 건, 널 찜했다는 뜻이야.')
    st.balloons()
