# 🌺 OAHU SHOP - 반응형 상품 랜딩페이지

오아후 샵의 신상품 26개를 소개하는 반응형 웹 애플리케이션입니다.

## 📋 주요 기능

### 사용자 페이지
- **메인 페이지**: 26개 신상품을 3열 그리드로 표시
- **상품 썸네일**: 각 상품 폴더의 두 번째 이미지를 썸네일로 사용
- **상품 상세 페이지**: 상품 클릭 시 모든 이미지를 3열 그리드로 표시
- **반응형 디자인**: 모바일, 태블릿, 데스크톱에 최적화
- **구글 시트 연동**: 상품 정보(상품명, 색상/사이즈, 가격) 실시간 로드

### 관리자 페이지
- **로그인 시스템**: 아이디/비밀번호 인증
  - 아이디: `oahu`
  - 비밀번호: `oahu123`
- **배너 관리**: 메인 페이지 배너 이미지 업로드 및 변경
- **상품 관리**: 구글 시트를 통한 상품 정보 수정
- **데이터 새로고침**: 캐시 초기화 기능

## 🚀 배포 방법

### Streamlit Cloud에 배포

1. **GitHub에 코드 업로드**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: OAHU Shop"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/oahu-shop.git
   git push -u origin main
   ```

2. **Streamlit Cloud 배포**
   - [Streamlit Cloud](https://streamlit.io/cloud)에 접속
   - "New app" 클릭
   - GitHub 저장소 연결
   - Main file: `app.py` 지정
   - Deploy 클릭

3. **환경 설정**
   - 자동으로 `requirements.txt`의 패키지 설치
   - 앱이 자동으로 실행됨

### 로컬 실행

```bash
# 의존성 설치
pip install -r requirements.txt

# 앱 실행
streamlit run app.py
```

## 📁 프로젝트 구조

```
oahu/
├── app.py                  # 메인 애플리케이션
├── requirements.txt        # Python 패키지 의존성
├── README.md              # 프로젝트 문서
├── .streamlit/
│   └── config.toml        # Streamlit 설정
└── image/                 # 상품 이미지 폴더
    ├── 126/              # 상품 1
    │   ├── image_1.jpg
    │   ├── image_2.jpg   # 썸네일로 사용
    │   └── ...
    ├── 127/              # 상품 2
    └── ...
```

## 🎨 상품 이미지 구조

- 각 폴더(126~151)는 하나의 상품을 나타냅니다
- 폴더 내 이미지는 자동으로 정렬되어 표시됩니다
- **썸네일**: 각 폴더의 두 번째 이미지(`image_2.jpg`)가 사용됩니다
- **상세 페이지**: 모든 이미지를 3열 그리드로 표시 (예: 15장 → 3x5)

## 📊 상품 정보 관리

상품 정보는 구글 시트에서 관리됩니다:

**[구글 시트 바로가기](https://docs.google.com/spreadsheets/d/1Cnd19QAMyNEgvEdfXTA1QtW0VMiTRMCBFGmrzKWezNQ/edit?usp=sharing)**

- **A열**: 상품명
- **B열**: 색상/사이즈 정보
- **C열**: 가격

구글 시트에서 정보를 수정하면 자동으로 웹 앱에 반영됩니다.

## 🔐 관리자 기능

관리자 페이지에서 다음 기능을 사용할 수 있습니다:

1. **배너 관리**: 메인 페이지 상단 배너 이미지 변경
2. **상품 정보 새로고침**: 구글 시트 변경사항 즉시 반영
3. **상품 목록 조회**: 현재 등록된 모든 상품 정보 확인

## 🖼️ 새 상품 추가 방법

1. `image/` 폴더에 새 폴더 생성 (예: `152/`)
2. 해당 폴더에 상품 이미지 업로드
3. 구글 시트에 해당 상품 정보 추가
4. 관리자 페이지에서 "상품 정보 새로고침" 클릭

## 💡 기술 스택

- **Frontend**: Streamlit (Python)
- **이미지 처리**: Pillow
- **데이터 관리**: Pandas, Google Sheets
- **배포**: Streamlit Cloud
- **버전 관리**: Git/GitHub

## 📱 반응형 디자인

- 모바일: 1열 레이아웃
- 태블릿: 2열 레이아웃
- 데스크톱: 3열 레이아웃

CSS Grid와 Flexbox를 활용한 완전 반응형 디자인

## 🔧 문제 해결

### 이미지가 표시되지 않는 경우
- 이미지 파일 형식이 JPG인지 확인
- 파일 권한 확인
- GitHub에 이미지가 정상적으로 업로드되었는지 확인

### 구글 시트 데이터가 로드되지 않는 경우
- 구글 시트가 "링크가 있는 모든 사용자" 권한으로 공개되어 있는지 확인
- 시트 ID가 올바른지 확인

## 📄 라이선스

이 프로젝트는 OAHU Shop의 소유입니다.

## 👤 개발자

OAHU Shop Development Team

---

**배포 완료 후 URL**: `https://your-app-name.streamlit.app`

