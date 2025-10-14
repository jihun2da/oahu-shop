# OAHU Shop - Git 초기화 및 GitHub 업로드 스크립트 (PowerShell)

Write-Host "🌺 OAHU Shop - GitHub 업로드 준비" -ForegroundColor Cyan
Write-Host "=" -Repeat 50 -ForegroundColor Cyan
Write-Host ""

# Git 초기화
Write-Host "📦 Git 초기화 중..." -ForegroundColor Yellow
git init

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Git 초기화 실패. Git이 설치되어 있는지 확인하세요." -ForegroundColor Red
    exit 1
}

# 모든 파일 추가
Write-Host "📁 파일 추가 중..." -ForegroundColor Yellow
git add .

# 커밋
Write-Host "💾 커밋 생성 중..." -ForegroundColor Yellow
git commit -m "Initial commit: OAHU Shop 반응형 랜딩페이지"

# 메인 브랜치로 변경
Write-Host "🌿 메인 브랜치 설정 중..." -ForegroundColor Yellow
git branch -M main

Write-Host ""
Write-Host "✅ Git 초기화 완료!" -ForegroundColor Green
Write-Host ""
Write-Host "다음 단계:" -ForegroundColor Cyan
Write-Host "1. GitHub에서 새 저장소를 생성하세요 (https://github.com/new)" -ForegroundColor White
Write-Host "2. 저장소를 Public으로 설정하세요" -ForegroundColor White
Write-Host "3. 아래 명령어를 실행하세요 (YOUR_USERNAME을 본인의 사용자명으로 변경):" -ForegroundColor White
Write-Host ""
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/oahu-shop.git" -ForegroundColor Yellow
Write-Host "   git push -u origin main" -ForegroundColor Yellow
Write-Host ""
Write-Host "4. Streamlit Cloud에서 배포하세요 (https://streamlit.io/cloud)" -ForegroundColor White
Write-Host ""
Write-Host "자세한 내용은 DEPLOYMENT.md 파일을 참고하세요." -ForegroundColor Cyan

