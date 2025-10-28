#!/bin/bash

# Deploy to Render - Pre-deployment Checklist Script
# Run this before pushing to ensure everything is configured correctly

echo "========================================="
echo "AI Resume Builder - Render Deployment"
echo "========================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if .env file exists
if [ ! -f .env ]; then
    echo -e "${YELLOW}⚠️  Warning: .env file not found${NC}"
    echo "   This is OK for Render (uses environment variables)"
else
    echo -e "${GREEN}✅ .env file found${NC}"
fi

# Check if migrations are up to date
echo ""
echo "Checking migrations..."
python manage.py makemigrations --dry-run --check > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Migrations are up to date${NC}"
else
    echo -e "${YELLOW}⚠️  Warning: You have unmade migrations${NC}"
    echo "   Run: python manage.py makemigrations"
fi

# Check if there are uncommitted changes
echo ""
echo "Checking Git status..."
if [ -z "$(git status --porcelain)" ]; then
    echo -e "${GREEN}✅ No uncommitted changes${NC}"
else
    echo -e "${YELLOW}⚠️  You have uncommitted changes:${NC}"
    git status --short
fi

# Test if Django can start
echo ""
echo "Testing Django configuration..."
python manage.py check --deploy > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Django configuration is valid${NC}"
else
    echo -e "${RED}❌ Django configuration has issues:${NC}"
    python manage.py check --deploy
fi

# Check requirements.txt
echo ""
echo "Checking requirements.txt..."
if [ -f requirements.txt ]; then
    echo -e "${GREEN}✅ requirements.txt found${NC}"
    echo "   Key packages:"
    grep -E "Django|gunicorn|psycopg2|whitenoise" requirements.txt | sed 's/^/   - /'
else
    echo -e "${RED}❌ requirements.txt not found${NC}"
fi

# Check build.sh
echo ""
echo "Checking build.sh..."
if [ -f build.sh ]; then
    echo -e "${GREEN}✅ build.sh found${NC}"
    if [ -x build.sh ]; then
        echo -e "${GREEN}✅ build.sh is executable${NC}"
    else
        echo -e "${YELLOW}⚠️  build.sh is not executable${NC}"
        echo "   Run: chmod +x build.sh"
    fi
else
    echo -e "${RED}❌ build.sh not found${NC}"
fi

# Summary
echo ""
echo "========================================="
echo "Pre-Deployment Checklist"
echo "========================================="
echo ""
echo "Before deploying to Render, ensure:"
echo ""
echo "1. Environment Variables Set on Render:"
echo "   - SECRET_KEY"
echo "   - DEBUG=False"
echo "   - ALLOWED_HOSTS=your-app.onrender.com"
echo "   - RENDER_EXTERNAL_HOSTNAME=your-app.onrender.com"
echo "   - DATABASE_URL (auto-set by Render PostgreSQL)"
echo "   - EMAIL_HOST_USER"
echo "   - EMAIL_HOST_PASSWORD (Gmail App Password)"
echo ""
echo "2. After Deployment:"
echo "   - Run migrations: python manage.py migrate"
echo "   - Create superuser: python manage.py createsuperuser"
echo "   - Test all pages: signup, login, password reset"
echo ""
echo "3. Monitor Logs:"
echo "   - Render Dashboard → Logs"
echo "   - Look for ✅ success or ❌ error messages"
echo ""
echo "========================================="
echo ""

# Ask if user wants to commit and push
read -p "Do you want to commit and push changes now? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    read -p "Enter commit message: " commit_msg
    
    if [ -z "$commit_msg" ]; then
        commit_msg="Fix 502 errors and improve authentication"
    fi
    
    echo ""
    echo "Committing changes..."
    git add .
    git commit -m "$commit_msg"
    
    echo ""
    echo "Pushing to origin main..."
    git push origin main
    
    echo ""
    echo -e "${GREEN}✅ Changes pushed successfully!${NC}"
    echo ""
    echo "Monitor deployment at: https://dashboard.render.com"
else
    echo ""
    echo "Skipping commit and push."
    echo "Run manually when ready:"
    echo "  git add ."
    echo "  git commit -m 'Your message'"
    echo "  git push origin main"
fi

echo ""
echo "========================================="
echo "Deployment script complete!"
echo "========================================="
