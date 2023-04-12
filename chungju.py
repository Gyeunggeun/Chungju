import streamlit as st


def 홈페이지():
    # 제목
    st.markdown("<h1 style='text-align: center; color: #FF5733; font-family: Malgun Gothic;'>청원생명</h1>", unsafe_allow_html=True)

    # 이미지 중앙 정렬
    image_url = "https://raw.githubusercontent.com/Gyeunggeun/Chungju/7a6d43a47041047a9219097cb46fb594d2fec634/%EC%A7%81%EC%A7%80%EC%83%B5.png" 
    markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 500px;'></div>"
    st.markdown(markdown_text, unsafe_allow_html=True)

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
    image_url = "https://raw.githubusercontent.com/Gyeunggeun/Chungju/7a6d43a47041047a9219097cb46fb594d2fec634/%EC%B2%AD%EC%9B%90%EC%83%9D%EB%AA%85%20%EC%9D%B8%EC%A6%9D%EB%A7%88%ED%81%AC.png"
    markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 500px;'></div>"
    st.markdown(markdown_text, unsafe_allow_html=True)


    # 청원생명 브랜드
    st.markdown("<h1 style='text-align: center; color: #FF5733; font-family: Arial;'>청원생명 브랜드</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #7B68EE; font-family: Arial;'>청원생명의 브랜드 설명</h3>", unsafe_allow_html=True)


    st.header('청원생명 소개')

    tab1, tab2 = st.tabs(['인증마크', '상세설명'])

    with tab1:
        st.caption('인증마크')
        image_url = "https://raw.githubusercontent.com/Gyeunggeun/Chungju/7a6d43a47041047a9219097cb46fb594d2fec634/%EC%B2%AD%EC%9B%90%EC%83%9D%EB%AA%85%20%EC%9D%B8%EC%A6%9D%EB%A7%88%ED%81%AC.png"
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 500px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.text('이 부분에는 청원생명 브랜드에 대한 인증마크에 대한 설명이 들어갈 예정입니다')

    with tab2:
        st.caption('상세설명')
        st.image('https://shop.ilovegohyang.go.kr/thumb/6666cd76f96956469e7be39d750cc7d9/860_244_44ba6bd969f981e1e3b1de19bb98.jpg')
        st.text('이 부분에는 청원생명 브랜드에 대한 상세 설명이 들어갈 예정입니다')

def 특산물():
    # 특산물 소개글 작성
    st.markdown("<h1 style='text-align: center; color: #FF5733; font-family: Arial;'>특산물</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('https://shop.ilovegohyang.go.kr/thumb/6666cd76f96956469e7be39d750cc7d9/860_244_44ba6bd969f981e1e3b1de19bb98.jpg')
        st.text('23년 직지쌀 10kg')
        original_price = '35,000원'
        discount_price = '28,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        # st.write("<s>100</s>    30000원", unsafe_allow_html=True)
        st.markdown(discount_html, unsafe_allow_html=True)
        # st.latex(r'''\sout{-10%}''')
    with col2:
        st.image('https://shop.ilovegohyang.go.kr/thumb/6666cd76f96956469e7be39d750cc7d9/860_244_44ba6bd969f981e1e3b1de19bb98.jpg')
        st.text('딸기 1KG')
        original_price = '25,000원'
        discount_price = '20,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
        
    with col3:
        st.image('https://raw.githubusercontent.com/Gyeunggeun/Chungju/2ca6cb3ded9cfa145b68bee05f86ea1eb843542a/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EA%B3%A0%EA%B5%AC%EB%A7%88_%EC%9B%90%EB%B3%B8.png')
        st.text('꿀 고구마 5KG')
        original_price = '30,000원'
        discount_price = '24,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
        
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('https://shop.ilovegohyang.go.kr/thumb/6666cd76f96956469e7be39d750cc7d9/860_244_44ba6bd969f981e1e3b1de19bb98.jpg')
        st.text('블루베리 1KG')
        original_price = '25,000원'
        discount_price = '20,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
        
    with col2:
        st.image('https://shop.ilovegohyang.go.kr/thumb/6666cd76f96956469e7be39d750cc7d9/860_244_44ba6bd969f981e1e3b1de19bb98.jpg')
        st.text('수박 5KG')
        original_price = '35,000원'
        discount_price = '28,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
        
    with col3:
        st.image('https://shop.ilovegohyang.go.kr/thumb/6666cd76f96956469e7be39d750cc7d9/860_244_44ba6bd969f981e1e3b1de19bb98.jpg')
        st.text('사과 10KG')
        original_price = '25,000원'
        discount_price = '19,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
        
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('https://shop.ilovegohyang.go.kr/thumb/6666cd76f96956469e7be39d750cc7d9/860_244_44ba6bd969f981e1e3b1de19bb98.jpg')
        st.text('토마토 5KG')
        original_price = '26,000원'
        discount_price = '22,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
        
    with col2:
        st.image('https://shop.ilovegohyang.go.kr/thumb/6666cd76f96956469e7be39d750cc7d9/860_244_44ba6bd969f981e1e3b1de19bb98.jpg')
        st.text('복숭아 3KG')
        original_price = '28,000원'
        discount_price = '23,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
        
    with col3:
        st.image('https://shop.ilovegohyang.go.kr/thumb/6666cd76f96956469e7be39d750cc7d9/860_244_44ba6bd969f981e1e3b1de19bb98.jpg')
        st.text('고당도 포도 3.5kg')
        original_price = '30,000원'
        discount_price = '25,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
                 
def 밀키트():
    # 특산물 소개글 작성
    st.markdown("<h1 style='text-align: center; color: #FF5733; font-family: Arial;'>밀키트</h1>", unsafe_allow_html=True)
   
        
        
def 특산품():
    # 특산물 소개글 작성
    

    tab1, tab2 = st.tabs(['인증마크', '상세설명'])

    with tab1:
        st.caption('인증마크')
        image_url = "https://raw.githubusercontent.com/Gyeunggeun/Chungju/7a6d43a47041047a9219097cb46fb594d2fec634/%EC%B2%AD%EC%9B%90%EC%83%9D%EB%AA%85%20%EC%9D%B8%EC%A6%9D%EB%A7%88%ED%81%AC.png"
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 500px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.text('이 부분에는 청원생명 브랜드에 대한 인증마크에 대한 설명이 들어갈 예정입니다')

    with tab2:
        st.caption('상세설명')
        st.image('https://shop.ilovegohyang.go.kr/thumb/6666cd76f96956469e7be39d750cc7d9/860_244_44ba6bd969f981e1e3b1de19bb98.jpg')
        st.text('이 부분에는 청원생명 브랜드에 대한 상세 설명이 들어갈 예정입니다')
        
        
page_names_to_funcs = {'홈페이지': 홈페이지, '청원생명이란?': 청원생명이란, '특산물': 특산물, '밀키트': 밀키트, '특산품':특산품}

selected_page = st.sidebar.selectbox('Select a page',page_names_to_funcs.keys())

page_names_to_funcs[selected_page]()