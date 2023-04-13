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
    st.markdown('<link href="https://fonts.googleapis.com/css?family=Noto+Sans+KR&display=swap" rel="stylesheet">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; font-family: Noto Sans KR;'>특산물</h1>", unsafe_allow_html=True)

    
    # st.markdown("<h1 style='text-align: center; color: #FF5733; font-family: Arial;'>특산물</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        image_url = 'https://raw.github.com/Gyeunggeun/Chungju/2ca6cb3ded9cfa145b68bee05f86ea1eb843542a/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%A7%81%EC%A7%80%EC%8C%80_%EB%B9%84%EC%9C%A8%EC%A1%B0%EC%A0%95.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 200px; height: 200px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
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
        image_url =   'https://raw.github.com/Gyeunggeun/Chungju/2ca6cb3ded9cfa145b68bee05f86ea1eb843542a/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%94%B8%EA%B8%B0_%EC%9B%90%EB%B3%B8.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 200px; height: 200px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.text('딸기 1KG')
        original_price = '25,000원'
        discount_price = '20,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
        
    with col3:
        image_url =  'https://raw.githubusercontent.com/Gyeunggeun/Chungju/2ca6cb3ded9cfa145b68bee05f86ea1eb843542a/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EA%B3%A0%EA%B5%AC%EB%A7%88_%EC%9B%90%EB%B3%B8.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 200px; height: 200px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
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
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/f33372d4dbdacfa398707644873322dc4c7e0984/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%B8%94%EB%A3%A8%EB%B2%A0%EB%A6%AC_%EC%9B%90%EB%B3%B8.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 200px; height: 200px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.text('블루베리 1KG')
        original_price = '25,000원'
        discount_price = '20,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
        
    with col2:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/a94c1543ee99a197ec46ddceae8be265a5fd93e8/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%88%98%EB%B0%95.png'
       
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 200px; height: 200px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.text('수박 5KG')
        original_price = '35,000원'
        discount_price = '28,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
        
    with col3:
        image_url ='https://raw.githubusercontent.com/Gyeunggeun/Chungju/f33372d4dbdacfa398707644873322dc4c7e0984/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%82%AC%EA%B3%BC_%EC%9B%90%EB%B3%B8.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 200px; height: 200px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
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
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/0060c3cf1aa3b1186e79bb6dfcc05ca929d978c0/%EC%9D%B4%EB%AF%B8%EC%A7%80/%ED%86%A0%EB%A7%88%ED%86%A0_%EC%9B%90%EB%B3%B8.png'
        
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 200px; height: 200px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.text('토마토 5KG')
        original_price = '26,000원'
        discount_price = '22,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
        
    with col2:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/f33372d4dbdacfa398707644873322dc4c7e0984/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%B3%B5%EC%88%AD%EC%95%84_%EC%9B%90%EB%B3%B8.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 200px; height: 200px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.text('복숭아 3KG')
        original_price = '28,000원'
        discount_price = '23,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
        
    with col3:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/a94c1543ee99a197ec46ddceae8be265a5fd93e8/%EC%9D%B4%EB%AF%B8%EC%A7%80/%ED%8F%AC%EB%8F%84_%EC%9B%90%EB%B3%B8.png'
        
        
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 200px; height: 200px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
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
    col1, col2 = st.columns(2)
    with col1:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/f33372d4dbdacfa398707644873322dc4c7e0984/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%94%B8%EA%B8%B0%EB%A7%89%EA%B1%B8%EB%A6%AC2.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 300px; height: 300px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.text('딸기 담금주')
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
        image_url ='https://raw.githubusercontent.com/Gyeunggeun/Chungju/f33372d4dbdacfa398707644873322dc4c7e0984/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%96%A1%EB%B3%B6%EC%9D%B4.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 300px; height: 300px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.text('떡볶이')
        original_price = '25,000원'
        discount_price = '20,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
    
        
    col1, col2 = st.columns(2)
    with col1:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/f33372d4dbdacfa398707644873322dc4c7e0984/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%95%A0%ED%98%B8%EB%B0%95%EC%A0%84.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 300px; height: 300px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.text('애호박전')
        original_price = '25,000원'
        discount_price = '20,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
        
    with col2:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/f33372d4dbdacfa398707644873322dc4c7e0984/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%96%A1%EB%B3%B6%EC%9D%B42.png'
       
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 300px; height: 300px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.text('고구마닭갈비')
        original_price = '35,000원'
        discount_price = '28,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/f33372d4dbdacfa398707644873322dc4c7e0984/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%9D%B4%EC%9C%A0%EC%9D%B4.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 300px; height: 300px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.text('청주 쌀 떡국')
        original_price = '12,000원'
        discount_price = '10,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)

    with col2:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/f33372d4dbdacfa398707644873322dc4c7e0984/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%9D%B4%EC%9C%A0%EC%9D%B4.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 300px; height: 300px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.text('해물누룽지탕')
        original_price = '13,000원'
        discount_price = '11,500원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
        
        
def 특산품():
    # 특산물 소개글 작성
    st.markdown("<h1 style='text-align: center; color: #FF5733; font-family: Arial;'>특산품</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/0060c3cf1aa3b1186e79bb6dfcc05ca929d978c0/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EA%B3%A0%EA%B5%AC%EB%A7%88%EB%96%A1.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 300px; height: 300px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.text('고구마 떡 1kg')
        original_price = '10,000원'
        discount_price = '8,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        # st.write("<s>100</s>    30000원", unsafe_allow_html=True)
        st.markdown(discount_html, unsafe_allow_html=True)
        # st.latex(r'''\sout{-10%}''')
    with col2:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/f33372d4dbdacfa398707644873322dc4c7e0984/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EA%B3%A0%EA%B5%AC%EB%A7%88%EA%B3%BC%EC%9E%90_%EC%9B%90%EB%B3%B8.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 300px; height: 300px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.text('고구마 과자')
        original_price = '5,000원'
        discount_price = '3,500원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        image_url = ' https://raw.githubusercontent.com/Gyeunggeun/Chungju/f33372d4dbdacfa398707644873322dc4c7e0984/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EA%B3%A0%EA%B5%AC%EB%A7%88%EC%8C%80%EC%B0%90%EB%B9%B5_%EC%9B%90%EB%B3%B8.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 300px; height: 300px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.text('고구마 쌀찐빵')
        original_price = '10,000원'
        discount_price = '8,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)

    with col2:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/d48d2b375027954d932954c7954082457f43c32f/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%9D%8C%EC%8B%9D/%EB%94%B8%EA%B8%B0%EB%8B%B4%EA%B8%88%EC%A3%BC.png'

        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 300px; height: 300px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.markdown("<h6 style='color:#FF5733; font-weight:bold;'>NEW!</h2>", unsafe_allow_html=True)
        st.text('딸기 담금주')
        original_price = '35,000원'
        discount_price = '28,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
        
        
page_names_to_funcs = {'홈페이지': 홈페이지, '청원생명이란?': 청원생명이란, '특산물': 특산물, '밀키트': 밀키트, '특산품':특산품}

selected_page = st.sidebar.selectbox('Select a page',page_names_to_funcs.keys())

page_names_to_funcs[selected_page]()