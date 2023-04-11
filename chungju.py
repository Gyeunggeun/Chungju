import streamlit as st


def 홈페이지():
    # 제목
    st.markdown("<h1 style='text-align: center; color: #FF5733; font-family: Arial;'>청원생명</h1>", unsafe_allow_html=True)

    # 이미지 로드
    image_url = "https://raw.githubusercontent.com/Gyeunggeun/Chungju/31f7238ac276891ff905ca1826209a9ea379352a/%EC%8A%AC%EB%9D%BC%EC%9D%B4%EB%93%9C1.PNG"
    # 이미지 중앙 배치
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image_url, width=500)

    st.markdown("<h3 style='text-align: center; font-family: Arial;'><br><br>이곳에는 청원생명에 대한 간단한 소개글이 올라갈 예정입니다</h3>",
                unsafe_allow_html=True)

    # # 배경 색상 변경
    # st.markdown(f"""
    #     <style>
    #         .stApp {{
    #             background-color: #FFFFFF;
    #         }}
    #     </style>
    # """, unsafe_allow_html=True)


def 청원생명이란():
    # 청원생명이란 무엇이고, 인증마크에 대한 소개글 작성
    st.markdown("<h1 style='text-align: center; color: #FF5733; font-family: Arial;'>청원생명이란?</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #7B68EE; font-family: Arial;'>청원생명은 청주의 프리미엄 식품 브랜드입니다.</h3>", unsafe_allow_html=True)
    st.image('https://post-phinf.pstatic.net/MjAyMjA1MTJfMjYz/MDAxNjUyMjgyNDMxNTMx.eiksoWq4rbopryxGcA8kYLbbluZBGmlgAyIqk9IGt5Ig.I7z63dT0QXrlv2VPs1lgrGniY-mDD3T8_PwOwDcSyBEg.PNG/%ED%94%BC%EC%B9%B4%EC%B8%84.png?type=w1200', width=500)


    # 청원생명 브랜드
    st.markdown("<h1 style='text-align: center; color: #FF5733; font-family: Arial;'>청원생명 브랜드</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #7B68EE; font-family: Arial;'>청원생명의 브랜드 설명</h3>", unsafe_allow_html=True)


    st.header('청원생명 소개')

    tab1, tab2 = st.tabs(['인증마크', '상세설명'])

    with tab1:
        st.caption('인증마크')
        st.image('https://www.seenews365.com/news/photo/202301/47777_55294_4050.jpg')
        st.text('이 부분에는 청원생명 브랜드에 대한 인증마크에 대한 설명이 들어갈 예정입니다')

    with tab2:
        st.caption('상세설명')
        st.image('https://shop.ilovegohyang.go.kr/thumb/6666cd76f96956469e7be39d750cc7d9/860_244_44ba6bd969f981e1e3b1de19bb98.jpg')
        st.text('이 부분에는 청원생명 브랜드에 대한 상세 설명이 들어갈 예정입니다')


page_names_to_funcs = {'홈페이지': 홈페이지, '청원생명이란?': 청원생명이란}

selected_page = st.sidebar.selectbox('Select a page',page_names_to_funcs.keys())

page_names_to_funcs[selected_page]()