import streamlit as st

# Noto Sans KR 글꼴 추가
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');
    </style>
""", unsafe_allow_html=True)


def 홈페이지():
    # 제목
    st.markdown("<h1 style='text-align: center; color: #006400; font-family: Noto Sans KR;'>직지마켓</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; font-family: Malgun Gothic;'><br>청주시의 프리미엄 식품 브랜드 청원생명의 물품을 판매하는 <br><br>직지마켓입니다.</h4>", unsafe_allow_html=True)

    # 이미지 중앙 정렬
    image_url = "https://raw.githubusercontent.com/Gyeunggeun/Chungju/dd768c6ca0abb8a5817ae8d0873c41f88f478569/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%A1%9C%EA%B3%A0/%EC%A7%81%EC%A7%80%EB%A7%88%EC%BC%93.png"
    markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 500px;'></div>"
    st.markdown(markdown_text, unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center; font-family: Malgun Gothic;'>청원생명과 함께 청주시의 프리미엄 브랜드를 체험하세요.</h4>",
                unsafe_allow_html=True)



def 청원생명이란():
    # 청원생명이란 무엇이고, 인증마크에 대한 소개글 작성
    st.markdown("<h1 style='text-align: center; color: #006400; font-family: Malgun-Gothic;'>청원생명이란?</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; font-family: Malgun-Gothic;'><br>청원생명은 청주의 프리미엄 식품 브랜드입니다.</h3>", unsafe_allow_html=True)
    image_url = "https://raw.githubusercontent.com/Gyeunggeun/Chungju/ff553a44b43e42badd58ce9c7dc7b0fe05fe11e9/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%A1%9C%EA%B3%A0/%EC%B2%AD%EC%9B%90%EC%83%9D%EB%AA%85%20%EC%B2%B4%ED%81%AC.png"
    markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 700px;'></div>"
    st.markdown(markdown_text, unsafe_allow_html=True)


    # 청원생명 브랜드
    st.markdown("<h2 style='text-align: center; color: #006400; font-family: Malgun-Gothic;'>청원생명 브랜드</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; font-family: Malgun-Gothic;'>인증마크 소개</h4>", unsafe_allow_html=True)


    st.markdown("<h2 style='color: #006400; font-family: Malgun-Gothic;'>청원생명 소개</h2>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(['인증마크', '상세설명'])

    with tab1:
        st.caption('인증마크')
        image_url = "https://raw.githubusercontent.com/Gyeunggeun/Chungju/c7bd8c0aaf5f96d0d23ba0da73aa792a7e4903e8/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%A1%9C%EA%B3%A0/%EC%B2%AD%EC%9B%90%EC%83%9D%EB%AA%85%EC%9D%B8%EC%A6%9D.png"
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 500px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.markdown("<h4 style=' text-align: center; font-family: Malgun Gothic; line-height: 1.5'>청주를 대표하는 삼색과 청원생명의 푸르른 자연환경과 맑은 물을 상징하는 청색의 조화를 통해 탄생한 인증마크입니다.<br><br>직지 마켓에서 구매한 제품 중 청원생명 인증마크를 확인하시면, 해당 제품이 청주지역에서 안전하게 생산되었으며, 청원생명의 엄격한 품질 기준을 통과했다는 것을 보장받을 수 있습니다.<br><br>이를 통해 더욱 신뢰성 높은 제품을 선택할 수 있으며, 지역 농업인들과 환경 보호에 기여할 수 있는 소비를 할 수 있습니다.</h4>", unsafe_allow_html=True)


    with tab2:
        st.caption('상세설명')
        st.markdown("<h5 style=' font-family: Noto Sans KR; line-height: 1.5'>직지마켓은 지농연도의 발전을 위해서는 농·특산물을 전국적으로 유통할 수 있는 서비스 입니다.<br><br>직지마켓은 D2C를 통한 특산품 가격 경쟁력 확보와 청원생명 인증을 통한 프리미엄화를 노리고 출범했습니다.<br><br>청주시의 농·특산물로만 활용해 청주시 대표 브랜드화 가능 지역 내에서 생산 상품으로 직지 마켓에서 핵심적으로 판매하고 있습니다. <br><br>직지마켓을 통해 청주시 인지도 상승 및 이미지 제고 효과가 있습니다. <br><br>우리는 직지마켓을 통해 일자리 창출, 농가 소득 증대 및 오프라인 매장으로 인한 청주시 관심 증대를 노리고 있습니다.</h5>",
        unsafe_allow_html=True)


def 특산물():
    # 특산물 소개글 작성
    st.markdown('<link href="https://fonts.googleapis.com/css?family=Noto+Sans+KR&display=swap" rel="stylesheet">', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #006400 ;font-family: Noto Sans KR;'>특산물</h1><br>", unsafe_allow_html=True)

    
    # st.markdown("<h1 style='text-align: center; color: #FF5733; font-family: Malgun-Gothic;'>특산물</h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        image_url = 'https://raw.github.com/Gyeunggeun/Chungju/2ca6cb3ded9cfa145b68bee05f86ea1eb843542a/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%A7%81%EC%A7%80%EC%8C%80_%EB%B9%84%EC%9C%A8%EC%A1%B0%EC%A0%95.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 200px; height: 200px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>23년 직지쌀 10kg</strong>
        """, unsafe_allow_html=True)
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
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>딸기 1kg</strong>
        """, unsafe_allow_html=True)
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
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>꿀고구마 5kg</strong>
        """, unsafe_allow_html=True)
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
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>블루베리 1kg</strong>
        """, unsafe_allow_html=True)
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
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>수박 5kg</strong>
        """, unsafe_allow_html=True)
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
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>사과 10kg</strong>
        """, unsafe_allow_html=True)
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
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>토마토 5kg</strong>
        """, unsafe_allow_html=True)
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
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>복숭아 3kg</strong>
        """, unsafe_allow_html=True)
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
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>고당도 포도 3.5kg</strong>
        """, unsafe_allow_html=True)
        original_price = '30,000원'
        discount_price = '25,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
                 
def 밀키트():
    # 특산물 소개글 작성
    
    st.markdown("<h1 style='text-align: center; color: #006400; font-family: Malgun-Gothic;'>밀키트</h1><br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/f33372d4dbdacfa398707644873322dc4c7e0984/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EB%94%B8%EA%B8%B0%EB%A7%89%EA%B1%B8%EB%A6%AC2.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 300px; height: 300px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>딸기 담금주</strong>
        """, unsafe_allow_html=True)
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
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>떡볶이</strong>
        """, unsafe_allow_html=True)
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
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>애호박전</strong>
        """, unsafe_allow_html=True)
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
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>고구마 닭갈비</strong>
        """, unsafe_allow_html=True)
        original_price = '35,000원'
        discount_price = '28,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/1cdaf953c6b8f21079c31e271a6792a4fad6bb96/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%9D%8C%EC%8B%9D/%EB%96%A1%EA%B5%AD%20%EB%B0%80%ED%82%A4%ED%8A%B8.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 300px; height: 300px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>청주 쌀 떡국</strong>
        """, unsafe_allow_html=True)
        original_price = '12,000원'
        discount_price = '10,000원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)

    with col2:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/1cdaf953c6b8f21079c31e271a6792a4fad6bb96/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%9D%8C%EC%8B%9D/%ED%95%B4%EB%AC%BC%EB%88%84%EB%A3%BD%EC%A7%80%ED%83%95.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 300px; height: 300px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>해물 누룽지탕</strong>
        """, unsafe_allow_html=True)
        original_price = '13,000원'
        discount_price = '11,500원'
        discount_html = f"""
        <span style='text-decoration: line-through; color: #a0a0a0; margin-right: 8px;'>{original_price}</span>
        <span style='font-weight: bold; color: #ff3e00;'>{discount_price}</span>
        """
        st.markdown(discount_html, unsafe_allow_html=True)
        
        
def 특산품():
    # 특산물 소개글 작성
    st.markdown("<h1 style='text-align: center; color: #006400; font-family: Malgun-Gothic;'>특산품</h1><br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/1cdaf953c6b8f21079c31e271a6792a4fad6bb96/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%9D%8C%EC%8B%9D/%EA%B3%A0%EA%B5%AC%EB%A7%88%EB%96%A11.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 300px; height: 300px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>고구마 떡 1kg</strong>
        """, unsafe_allow_html=True)
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
        image_url = 'https://raw.githubusercontent.com/Gyeunggeun/Chungju/1cdaf953c6b8f21079c31e271a6792a4fad6bb96/%EC%9D%B4%EB%AF%B8%EC%A7%80/%EC%9D%8C%EC%8B%9D/%EA%B3%A0%EA%B5%AC%EB%A7%88%EA%B3%BC%EC%9E%90_%EC%95%84%EC%9D%B4%EC%9A%A9.png'
        markdown_text = f"<div style='text-align:center'><img src='{image_url}' style='width: 300px; height: 300px;'></div>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>고구마 과자</strong>
        """, unsafe_allow_html=True)
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
        st.markdown("""
            <br><strong style='font-family: Noto Sans KR;'>고구마 쌀 찐빵</strong>
        """, unsafe_allow_html=True)
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
        st.markdown("<h6 style='color:#FF5733; font-weight:bold;'>NEW!</h6>", unsafe_allow_html=True)
        st.markdown("""
            <strong style='font-family: Noto Sans KR;'>딸기 담금주</strong>
        """, unsafe_allow_html=True)
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