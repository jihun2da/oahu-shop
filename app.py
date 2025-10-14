import streamlit as st
import pandas as pd
from pathlib import Path
import os
from PIL import Image
import io

# 페이지 설정
st.set_page_config(
    page_title="OAHU Shop",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS 스타일링
st.markdown("""
<style>
    /* 전체 페이지 스타일 */
    .main {
        background-color: #ffffff;
    }
    
    /* 헤더 스타일 */
    .header {
        background-color: #000000;
        color: white;
        padding: 20px;
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 30px;
    }
    
    /* 상품 카드 스타일 */
    .product-card {
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
        background-color: white;
        height: 100%;
    }
    
    .product-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    .product-name {
        font-size: 16px;
        font-weight: 600;
        margin-top: 10px;
        color: #333;
    }
    
    .product-info {
        font-size: 14px;
        color: #666;
        margin-top: 5px;
    }
    
    .product-price {
        font-size: 18px;
        font-weight: bold;
        color: #e91e63;
        margin-top: 8px;
    }
    
    /* 이미지 갤러리 스타일 */
    .gallery-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
        padding: 20px 0;
    }
    
    /* 버튼 스타일 */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #000000;
        color: white;
        padding: 10px 20px;
        font-weight: 600;
    }
    
    .stButton>button:hover {
        background-color: #333333;
    }
    
    /* 배너 스타일 */
    .banner {
        width: 100%;
        height: 400px;
        object-fit: cover;
        margin-bottom: 40px;
    }
    
    /* 로그인 폼 스타일 */
    .login-container {
        max-width: 400px;
        margin: 100px auto;
        padding: 40px;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        background-color: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# 세션 스테이트 초기화
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_product' not in st.session_state:
    st.session_state.selected_product = None
if 'banner_image' not in st.session_state:
    st.session_state.banner_image = None
if 'products_data' not in st.session_state:
    st.session_state.products_data = None

# 관리자 계정 정보
ADMIN_USERNAME = "oahu"
ADMIN_PASSWORD = "oahu123"

# 구글 시트 데이터 로드
@st.cache_data
def load_google_sheet_data():
    try:
        # 구글 시트 ID
        sheet_id = "1Cnd19QAMyNEgvEdfXTA1QtW0VMiTRMCBFGmrzKWezNQ"
        # CSV export URL
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
        df = pd.read_csv(url)
        return df
    except Exception as e:
        st.error(f"데이터 로드 중 오류 발생: {e}")
        # 폴백 데이터
        return pd.DataFrame({
            'A': [f'상품 {i}' for i in range(126, 152)],
            'B': [f'색상/사이즈 정보 {i}' for i in range(126, 152)],
            'C': [f'{50000 + i*1000}원' for i in range(26)]
        })

# 이미지 폴더 스캔
def get_product_folders():
    image_path = Path("image")
    if not image_path.exists():
        return []
    folders = sorted([f for f in image_path.iterdir() if f.is_dir()])
    return folders

# 폴더의 이미지 파일 가져오기
def get_folder_images(folder_path):
    images = sorted([f for f in folder_path.glob("*.jpg") if f.name != "ㅎ.jpg"])
    return images

# 썸네일 이미지 가져오기 (두 번째 이미지)
def get_thumbnail(folder_path):
    images = get_folder_images(folder_path)
    if len(images) >= 2:
        return images[1]  # 두 번째 이미지
    elif len(images) > 0:
        return images[0]  # 이미지가 하나면 첫 번째
    return None

# 메인 페이지
def show_main_page():
    # 헤더
    st.markdown('<div class="header">🌺 OAHU SHOP 🌺</div>', unsafe_allow_html=True)
    
    # 배너 이미지
    if st.session_state.banner_image:
        st.image(st.session_state.banner_image, use_container_width=True)
    else:
        # 기본 배너
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    height: 300px; display: flex; align-items: center; justify-content: center;
                    margin-bottom: 40px; border-radius: 12px;">
            <h1 style="color: white; font-size: 48px; font-weight: bold;">NEW ARRIVALS</h1>
        </div>
        """, unsafe_allow_html=True)
    
    # 데이터 로드
    df = load_google_sheet_data()
    folders = get_product_folders()
    
    if not folders:
        st.warning("상품 폴더를 찾을 수 없습니다.")
        return
    
    st.markdown("### 신상품")
    st.markdown("---")
    
    # 3열 그리드로 상품 표시
    cols_per_row = 3
    for i in range(0, len(folders), cols_per_row):
        cols = st.columns(cols_per_row)
        
        for j, col in enumerate(cols):
            idx = i + j
            if idx >= len(folders):
                break
            
            folder = folders[idx]
            folder_num = folder.name
            
            with col:
                # 썸네일 이미지
                thumbnail = get_thumbnail(folder)
                if thumbnail:
                    try:
                        img = Image.open(thumbnail)
                        st.image(img, use_container_width=True)
                    except:
                        st.info("이미지를 불러올 수 없습니다.")
                
                # 상품 정보
                row_idx = idx
                if row_idx < len(df):
                    product_name = df.iloc[row_idx, 0] if len(df.columns) > 0 else f"상품 {folder_num}"
                    product_info = df.iloc[row_idx, 1] if len(df.columns) > 1 else "정보 없음"
                    product_price = df.iloc[row_idx, 2] if len(df.columns) > 2 else "가격 문의"
                else:
                    product_name = f"상품 {folder_num}"
                    product_info = "정보 없음"
                    product_price = "가격 문의"
                
                st.markdown(f'<div class="product-name">{product_name}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="product-info">{product_info}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="product-price">{product_price}</div>', unsafe_allow_html=True)
                
                if st.button("상세보기", key=f"btn_{folder_num}"):
                    st.session_state.selected_product = folder
                    st.session_state.page = 'detail'
                    st.rerun()
    
    # 관리자 로그인 링크
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🔐 관리자 페이지"):
            st.session_state.page = 'login'
            st.rerun()

# 상품 상세 페이지
def show_detail_page():
    if not st.session_state.selected_product:
        st.session_state.page = 'home'
        st.rerun()
        return
    
    folder = st.session_state.selected_product
    folder_num = folder.name
    
    # 뒤로가기 버튼
    if st.button("← 목록으로 돌아가기"):
        st.session_state.page = 'home'
        st.session_state.selected_product = None
        st.rerun()
    
    st.markdown("---")
    
    # 상품 정보
    df = load_google_sheet_data()
    folders = get_product_folders()
    folder_idx = folders.index(folder) if folder in folders else 0
    
    if folder_idx < len(df):
        product_name = df.iloc[folder_idx, 0] if len(df.columns) > 0 else f"상품 {folder_num}"
        product_info = df.iloc[folder_idx, 1] if len(df.columns) > 1 else "정보 없음"
        product_price = df.iloc[folder_idx, 2] if len(df.columns) > 2 else "가격 문의"
    else:
        product_name = f"상품 {folder_num}"
        product_info = "정보 없음"
        product_price = "가격 문의"
    
    st.markdown(f"# {product_name}")
    st.markdown(f"**색상/사이즈:** {product_info}")
    st.markdown(f"**가격:** {product_price}")
    st.markdown("---")
    
    # 이미지 갤러리
    images = get_folder_images(folder)
    
    if not images:
        st.warning("상품 이미지가 없습니다.")
        return
    
    # 3열 그리드로 모든 이미지 표시
    cols_per_row = 3
    for i in range(0, len(images), cols_per_row):
        cols = st.columns(cols_per_row)
        
        for j, col in enumerate(cols):
            idx = i + j
            if idx >= len(images):
                break
            
            with col:
                try:
                    img = Image.open(images[idx])
                    st.image(img, use_container_width=True, caption=images[idx].name)
                except Exception as e:
                    st.error(f"이미지 로드 실패: {e}")

# 로그인 페이지
def show_login_page():
    st.markdown('<div class="header">🔐 관리자 로그인</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        
        username = st.text_input("아이디", placeholder="아이디를 입력하세요")
        password = st.text_input("비밀번호", type="password", placeholder="비밀번호를 입력하세요")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            if st.button("로그인", use_container_width=True):
                if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                    st.session_state.logged_in = True
                    st.session_state.page = 'admin'
                    st.success("로그인 성공!")
                    st.rerun()
                else:
                    st.error("아이디 또는 비밀번호가 올바르지 않습니다.")
        
        with col_b:
            if st.button("취소", use_container_width=True):
                st.session_state.page = 'home'
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

# 관리자 페이지
def show_admin_page():
    if not st.session_state.logged_in:
        st.session_state.page = 'login'
        st.rerun()
        return
    
    st.markdown('<div class="header">⚙️ 관리자 페이지</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("← 메인 페이지로"):
            st.session_state.page = 'home'
            st.rerun()
    
    with col2:
        if st.button("로그아웃"):
            st.session_state.logged_in = False
            st.session_state.page = 'home'
            st.rerun()
    
    st.markdown("---")
    
    # 탭 메뉴
    tab1, tab2, tab3 = st.tabs(["📸 배너 관리", "📦 상품 관리", "🖼️ 이미지 업로드"])
    
    with tab1:
        st.subheader("배너 이미지 관리")
        st.markdown("메인 페이지 상단에 표시될 배너 이미지를 업로드하세요.")
        
        uploaded_banner = st.file_uploader("배너 이미지 선택", type=['jpg', 'jpeg', 'png'], key="banner_upload")
        
        if uploaded_banner:
            st.image(uploaded_banner, caption="미리보기", use_container_width=True)
            if st.button("배너 적용"):
                st.session_state.banner_image = uploaded_banner
                st.success("배너가 업데이트되었습니다!")
        
        if st.session_state.banner_image:
            if st.button("배너 제거"):
                st.session_state.banner_image = None
                st.success("배너가 제거되었습니다!")
                st.rerun()
    
    with tab2:
        st.subheader("상품 정보 관리")
        st.markdown("""
        상품 정보는 구글 시트에서 관리됩니다.
        
        **[구글 시트 바로가기](https://docs.google.com/spreadsheets/d/1Cnd19QAMyNEgvEdfXTA1QtW0VMiTRMCBFGmrzKWezNQ/edit?usp=sharing)**
        
        - **A열**: 상품명
        - **B열**: 색상/사이즈
        - **C열**: 가격
        
        구글 시트에서 정보를 수정한 후 아래 버튼을 클릭하여 새로고침하세요.
        """)
        
        if st.button("🔄 상품 정보 새로고침"):
            st.cache_data.clear()
            st.success("상품 정보가 새로고침되었습니다!")
            st.rerun()
        
        # 현재 상품 목록 표시
        st.markdown("---")
        st.markdown("#### 현재 등록된 상품 목록")
        df = load_google_sheet_data()
        st.dataframe(df, use_container_width=True)
    
    with tab3:
        st.subheader("상품 이미지 업로드")
        st.markdown("""
        현재 Streamlit Cloud에서는 파일 업로드 기능이 제한됩니다.
        
        **이미지 추가 방법:**
        1. GitHub 저장소의 `image/` 폴더에 접속
        2. 새 폴더 생성 (폴더명은 숫자, 예: 152, 153...)
        3. 해당 폴더에 상품 이미지 업로드
        4. 구글 시트에 상품 정보 추가
        
        **참고:** 각 폴더의 두 번째 이미지(image_2.jpg)가 썸네일로 사용됩니다.
        """)
        
        st.info("로컬 환경에서는 이미지 폴더를 직접 수정할 수 있습니다.")

# 메인 라우팅
def main():
    page = st.session_state.page
    
    if page == 'home':
        show_main_page()
    elif page == 'detail':
        show_detail_page()
    elif page == 'login':
        show_login_page()
    elif page == 'admin':
        show_admin_page()
    else:
        show_main_page()

if __name__ == "__main__":
    main()

