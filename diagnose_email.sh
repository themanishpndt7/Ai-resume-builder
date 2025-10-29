#!/bin/bash

echo "========================================================================"
echo "🔍 EMAIL CONFIGURATION TROUBLESHOOTER"
echo "========================================================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "Step 1: Checking local .env file..."
echo "------------------------------------------------------------------------"

if [ -f .env ]; then
    echo -e "${GREEN}✅ .env file exists${NC}"
    
    # Check for email variables
    EMAIL_VARS=("EMAIL_HOST" "EMAIL_PORT" "EMAIL_USE_TLS" "EMAIL_HOST_USER" "EMAIL_HOST_PASSWORD")
    MISSING=0
    
    for var in "${EMAIL_VARS[@]}"; do
        if grep -q "^${var}=" .env; then
            if [ "$var" == "EMAIL_HOST_PASSWORD" ]; then
                echo -e "${GREEN}✅ $var is set${NC}"
            else
                VALUE=$(grep "^${var}=" .env | cut -d'=' -f2-)
                echo -e "${GREEN}✅ $var = $VALUE${NC}"
            fi
        else
            echo -e "${RED}❌ $var is NOT set${NC}"
            MISSING=$((MISSING + 1))
        fi
    done
    
    if [ $MISSING -eq 0 ]; then
        echo -e "\n${GREEN}✅ All email variables are set in .env file${NC}"
    else
        echo -e "\n${RED}❌ $MISSING variable(s) missing in .env file${NC}"
    fi
else
    echo -e "${RED}❌ .env file NOT found!${NC}"
fi

echo ""
echo "========================================================================"
echo "Step 2: IMPORTANT - Render Configuration"
echo "========================================================================"
echo ""
echo -e "${YELLOW}⚠️  The .env file is LOCAL ONLY and NOT deployed to Render!${NC}"
echo ""
echo "You MUST add these variables to Render Dashboard:"
echo ""
echo "1. Go to: https://dashboard.render.com/"
echo "2. Select: ai-resume-builder-6jan"
echo "3. Click: Environment tab"
echo "4. Add these 5 variables:"
echo ""
echo "   EMAIL_HOST = smtp.gmail.com"
echo "   EMAIL_PORT = 587"
echo "   EMAIL_USE_TLS = True"
echo "   EMAIL_HOST_USER = your-email@example.com"
echo "   EMAIL_HOST_PASSWORD = <YOUR_APP_PASSWORD>"
echo ""
echo "5. Click 'Save Changes'"
echo "6. Wait 2-3 minutes for redeploy"
echo ""

echo "========================================================================"
echo "Step 3: Verification"
echo "========================================================================"
echo ""
echo "After adding variables to Render, check:"
echo ""
echo "1. Check Render Logs:"
echo "   Should show: '✅ Email configured: Real emails will be sent via SMTP'"
echo ""
echo "2. Check Email Config Status:"
echo "   Visit: https://ai-resume-builder-6jan.onrender.com/check-email-config/"
echo "   Should show: 'is_properly_configured': true"
echo ""
echo "3. Test Password Reset:"
echo "   Visit: https://ai-resume-builder-6jan.onrender.com/accounts/password/reset/"
echo "   Enter email and request OTP"
echo "   Check inbox (and spam folder)"
echo ""

echo "========================================================================"
echo "Quick Test Commands:"
echo "========================================================================"
echo ""
echo "Check email config from command line:"
echo "  curl https://ai-resume-builder-6jan.onrender.com/check-email-config/"
echo ""
echo "Run local diagnostic:"
echo "  python3 check_env_email.py"
echo ""

echo "========================================================================"
echo "Need Help?"
echo "========================================================================"
echo ""
echo "If OTP still not working after adding to Render:"
echo ""
echo "1. Verify all 5 variables are in Render (no typos)"
echo "2. Check Render logs for error messages"
echo "3. Verify Gmail App Password is still valid"
echo "4. Try testing with a different email address"
echo "5. Check spam/junk folder"
echo ""
echo "========================================================================"
