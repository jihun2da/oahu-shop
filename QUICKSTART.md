# 🚀 빠른 시작 가이드

## 로컬에서 실행하기

### 필수 요구사항
- Python 3.8 이상
- pip (Python 패키지 관리자)

### 1단계: 패키지 설치

```bash
pip install -r requirements.txt
```

### 2단계: 앱 실행

```bash
streamlit run app.py
```

브라우저가 자동으로 열립니다. 열리지 않으면 `http://localhost:8501`에 접속하세요.

## 기능 테스트

### 사용자 기능
1. **메인 페이지**: 26개 상품 목록 확인
2. **상품 클릭**: 상세 페이지에서 모든 이미지 확인
3. **반응형**: 브라우저 크기를 조절해보세요

### 관리자 기능
1. 메인 페이지 하단의 "🔐 관리자 페이지" 클릭
2. 로그인 정보 입력:
   - 아이디: `oahu`
   - 비밀번호: `oahu123`
3. 배너 관리, 상품 정보 새로고침 등 테스트

## GitHub에 업로드하기

### Windows (PowerShell)
```powershell
.\setup_git.ps1
```

### Mac/Linux (Bash)
```bash
chmod +x setup_git.sh
./setup_git.sh
```

또는 수동으로:

```bash
git init
git add .
git commit -m "Initial commit: OAHU Shop"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/oahu-shop.git
git push -u origin main
```

## Streamlit Cloud 배포

1. [Streamlit Cloud](https://streamlit.io/cloud) 접속
2. GitHub 계정으로 로그인
3. "New app" 클릭
4. 저장소 선택: `YOUR_USERNAME/oahu-shop`
5. Main file: `app.py`
6. "Deploy!" 클릭

배포 완료까지 약 2-5분 소요됩니다.

## 상품 정보 수정

1. [구글 시트](https://docs.google.com/spreadsheets/d/1Cnd19QAMyNEgvEdfXTA1QtW0VMiTRMCBFGmrzKWezNQ/edit?usp=sharing) 열기
2. 데이터 수정:
   - **A열**: 상품명
   - **B열**: 색상/사이즈
   - **C열**: 가격
3. 앱의 관리자 페이지에서 "상품 정보 새로고침" 클릭

## 새 상품 추가

1. `image/` 폴더에 새 폴더 생성 (예: `152/`)
2. 상품 이미지를 해당 폴더에 추가
3. 구글 시트에 상품 정보 추가
4. GitHub에 푸시:
   ```bash
   git add .
   git commit -m "Add new product"
   git push
   ```
5. Streamlit Cloud가 자동으로 재배포

## 문제 해결

### 이미지가 표시되지 않음
- `image/` 폴더 구조 확인
- 이미지 파일 형식 확인 (JPG)

### 구글 시트 데이터 로드 실패
- 시트가 공개 설정되어 있는지 확인
- 인터넷 연결 확인

### 배포 실패
- `requirements.txt` 확인
- Streamlit Cloud 로그 확인

---

더 자세한 내용은 `DEPLOYMENT.md`를 참고하세요.

