# 🚀 OAHU Shop - 배포 가이드

## GitHub에 업로드하기

### 1단계: Git 저장소 초기화

터미널에서 프로젝트 폴더로 이동한 후 다음 명령어를 실행하세요:

```bash
# Git 초기화
git init

# 모든 파일 추가
git add .

# 커밋
git commit -m "Initial commit: OAHU Shop 반응형 랜딩페이지"

# 메인 브랜치 설정
git branch -M main
```

### 2단계: GitHub 저장소 생성

1. [GitHub](https://github.com)에 로그인
2. 오른쪽 상단의 `+` 버튼 클릭 → `New repository` 선택
3. Repository 이름 입력 (예: `oahu-shop`)
4. Public으로 설정 (Streamlit Cloud는 공개 저장소 필요)
5. **Initialize this repository with README 체크하지 않기**
6. `Create repository` 클릭

### 3단계: GitHub에 푸시

GitHub에서 생성한 저장소 URL을 복사한 후:

```bash
# 원격 저장소 추가 (YOUR_USERNAME을 본인의 GitHub 사용자명으로 변경)
git remote add origin https://github.com/YOUR_USERNAME/oahu-shop.git

# 푸시
git push -u origin main
```

**중요**: 이미지 파일이 많을 경우 푸시에 시간이 걸릴 수 있습니다.

## Streamlit Cloud에 배포하기

### 1단계: Streamlit Cloud 접속

1. [Streamlit Cloud](https://streamlit.io/cloud)에 접속
2. GitHub 계정으로 로그인

### 2단계: 새 앱 배포

1. 대시보드에서 `New app` 버튼 클릭
2. 배포 설정:
   - **Repository**: `YOUR_USERNAME/oahu-shop` 선택
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL**: 원하는 URL 설정 (예: `oahu-shop`)

3. `Deploy!` 버튼 클릭

### 3단계: 배포 완료

- 자동으로 `requirements.txt`의 패키지 설치
- 앱 빌드 및 실행
- 배포 완료까지 약 2-5분 소요
- 완료 후 URL: `https://your-app-name.streamlit.app`

## 구글 시트 권한 설정

배포 전 구글 시트 권한을 확인하세요:

1. [구글 시트](https://docs.google.com/spreadsheets/d/1Cnd19QAMyNEgvEdfXTA1QtW0VMiTRMCBFGmrzKWezNQ/edit?usp=sharing) 열기
2. 오른쪽 상단 `공유` 버튼 클릭
3. `일반 액세스` → `링크가 있는 모든 사용자`로 설정
4. 권한: `뷰어` 또는 `편집자`
5. 완료 클릭

## 로컬 테스트

배포 전 로컬에서 먼저 테스트해보세요:

```bash
# 가상환경 생성 (선택사항)
python -m venv venv

# 가상환경 활성화
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 패키지 설치
pip install -r requirements.txt

# 앱 실행
streamlit run app.py
```

브라우저에서 자동으로 `http://localhost:8501` 열림

## 업데이트 배포

코드를 수정한 후 다시 배포하려면:

```bash
# 변경사항 추가
git add .

# 커밋
git commit -m "설명 메시지"

# 푸시
git push
```

Streamlit Cloud는 자동으로 변경사항을 감지하고 재배포합니다.

## 문제 해결

### 이미지가 너무 커서 GitHub에 업로드되지 않는 경우

GitHub는 100MB 이상의 파일을 거부합니다. 이미지 크기를 줄이거나 Git LFS를 사용하세요:

```bash
# Git LFS 설치
git lfs install

# 이미지 파일 추적
git lfs track "*.jpg"
git lfs track "*.jpeg"
git lfs track "*.png"

# .gitattributes 파일 추가
git add .gitattributes

# 커밋 및 푸시
git commit -m "Add Git LFS support"
git push
```

### Streamlit Cloud 빌드 실패

1. `requirements.txt` 파일 확인
2. Python 버전 호환성 확인
3. Streamlit Cloud 로그 확인

### 구글 시트 데이터가 로드되지 않음

1. 시트가 공개 설정되어 있는지 확인
2. 시트 ID가 올바른지 확인
3. 인터넷 연결 확인

## 관리자 계정 보안

프로덕션 환경에서는 Streamlit Secrets를 사용하세요:

1. Streamlit Cloud 대시보드에서 앱 설정 열기
2. `Secrets` 섹션으로 이동
3. 다음 내용 추가:

```toml
[admin]
username = "oahu"
password = "oahu123"
```

4. `app.py` 수정:

```python
# 기존 코드 대신
ADMIN_USERNAME = st.secrets["admin"]["username"]
ADMIN_PASSWORD = st.secrets["admin"]["password"]
```

## 도메인 연결 (선택사항)

Streamlit Cloud Pro 계정이 있다면 커스텀 도메인을 연결할 수 있습니다:

1. 도메인 DNS 설정에서 CNAME 레코드 추가
2. Streamlit Cloud 앱 설정에서 도메인 추가
3. SSL 인증서 자동 생성

---

**배포 성공!** 🎉

이제 전 세계 어디서나 OAHU Shop에 접속할 수 있습니다.

