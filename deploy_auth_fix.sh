#!/bin/bash

# AI Resume Builder - Authentication Fix Deployment Script
# This script deploys the complete authentication system fix

echo "🚀 AI Resume Builder - Authentication Fix Deployment"
echo "=================================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Step 1: Check if we're in the right directory
if [ ! -f "manage.py" ]; then
    echo -e "${RED}❌ Error: manage.py not found. Please run this script from the project root.${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Project directory verified${NC}"
echo ""

# Step 2: Create migrations
echo "📦 Creating database migrations..."
python3 manage.py makemigrations users
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Migrations created successfully${NC}"
else
    echo -e "${RED}❌ Failed to create migrations${NC}"
    exit 1
fi
echo ""

# Step 3: Apply migrations
echo "🔄 Applying migrations to database..."
python3 manage.py migrate
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Migrations applied successfully${NC}"
else
    echo -e "${RED}❌ Failed to apply migrations${NC}"
    exit 1
fi
echo ""

# Step 4: Collect static files (for production)
echo "📁 Collecting static files..."
python3 manage.py collectstatic --noinput
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Static files collected${NC}"
else
    echo -e "${YELLOW}⚠️  Warning: Failed to collect static files (may not be critical)${NC}"
fi
echo ""

# Step 5: Check email configuration
echo "📧 Checking email configuration..."
if [ -z "$EMAIL_HOST_USER" ] || [ -z "$EMAIL_HOST_PASSWORD" ]; then
    echo -e "${YELLOW}⚠️  Warning: Email credentials not configured${NC}"
    echo "   Set EMAIL_HOST_USER and EMAIL_HOST_PASSWORD environment variables"
    echo "   OTP emails will be printed to console instead"
else
    echo -e "${GREEN}✅ Email configuration found${NC}"
fi
echo ""

# Step 6: Summary
echo "=================================================="
echo "🎉 Authentication System Fix Deployed Successfully!"
echo "=================================================="
echo ""
echo "✅ What's been fixed:"
echo "   • Signup with OTP email verification"
echo "   • Login with welcome message"
echo "   • Password reset with 5-minute OTP"
echo "   • Logout with proper session cleanup"
echo "   • Clean UI without premature errors"
echo ""
echo "📋 Next Steps:"
echo "   1. Test locally: python3 manage.py runserver"
echo "   2. Visit: http://localhost:8000/accounts/signup/"
echo "   3. Test signup → OTP → login flow"
echo "   4. If all works, commit and push to Render"
echo ""
echo "🔧 For Render deployment:"
echo "   git add ."
echo "   git commit -m 'Fix: Complete authentication with OTP verification'"
echo "   git push origin main"
echo ""
echo "📖 Read AUTHENTICATION_COMPLETE_FIX.md for full documentation"
echo ""
