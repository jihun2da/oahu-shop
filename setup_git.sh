#!/bin/bash
# OAHU Shop - Git 초기화 및 GitHub 업로드 스크립트 (Bash)

echo "🌺 OAHU Shop - GitHub 업로드 준비"
echo "=================================================="
echo ""

# Git 초기화
echo "📦 Git 초기화 중..."
git init

if [ $? -ne 0 ]; then
    echo "❌ Git 초기화 실패. Git이 설치되어 있는지 확인하세요."
    exit 1
fi

# 모든 파일 추가
echo "📁 파일 추가 중..."
git add .

# 커밋
echo "💾 커밋 생성 중..."
git commit -m "Initial commit: OAHU Shop 반응형 랜딩페이지"

# 메인 브랜치로 변경
echo "🌿 메인 브랜치 설정 중..."
git branch -M main

echo ""
echo "✅ Git 초기화 완료!"
echo ""
echo "다음 단계:"
echo "1. GitHub에서 새 저장소를 생성하세요 (https://github.com/new)"
echo "2. 저장소를 Public으로 설정하세요"
echo "3. 아래 명령어를 실행하세요 (YOUR_USERNAME을 본인의 사용자명으로 변경):"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/oahu-shop.git"
echo "   git push -u origin main"
echo ""
echo "4. Streamlit Cloud에서 배포하세요 (https://streamlit.io/cloud)"
echo ""
echo "자세한 내용은 DEPLOYMENT.md 파일을 참고하세요."

