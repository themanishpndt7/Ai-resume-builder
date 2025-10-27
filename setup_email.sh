#!/bin/bash

# Quick Setup Script for Real Email Sending
# Run this script to configure email for password reset

echo "=========================================="
echo "📧 EMAIL SETUP FOR PASSWORD RESET"
echo "=========================================="
echo ""
echo "This script will help you configure real email sending."
echo ""
echo "Choose your setup method:"
echo ""
echo "1. 🚀 Automatic Configuration (Recommended)"
echo "   - Interactive setup wizard"
echo "   - Guided step-by-step"
echo ""
echo "2. 📖 Manual Setup Instructions"
echo "   - View detailed guide"
echo "   - Configure manually"
echo ""
echo "3. 🧪 Test Current Configuration"
echo "   - Check if email is working"
echo "   - Send test email"
echo ""
echo "4. ❌ Exit"
echo ""

read -p "Enter choice (1-4): " choice

case $choice in
    1)
        echo ""
        echo "🚀 Starting automatic configuration..."
        echo ""
        python3 configure_email.py
        ;;
    2)
        echo ""
        echo "📖 Opening setup guide..."
        echo ""
        if command -v less &> /dev/null; then
            less EMAIL_SETUP_GUIDE.md
        else
            cat EMAIL_SETUP_GUIDE.md
        fi
        ;;
    3)
        echo ""
        echo "🧪 Testing email configuration..."
        echo ""
        python3 test_email_sending.py
        ;;
    4)
        echo ""
        echo "👋 Goodbye!"
        exit 0
        ;;
    *)
        echo ""
        echo "❌ Invalid choice!"
        exit 1
        ;;
esac

echo ""
echo "=========================================="
echo "Next Steps:"
echo "=========================================="
echo ""
echo "1. If configuration successful, restart server:"
echo "   python3 manage.py runserver"
echo ""
echo "2. Test password reset at:"
echo "   http://localhost:8000/accounts/login/"
echo ""
echo "3. Check your email inbox for reset link"
echo ""
