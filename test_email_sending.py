#!/usr/bin/env python3
"""
Test Email Sending Configuration

This script tests if your email configuration is working correctly.
"""

import os
import sys
import django

# Setup Django environment
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.core.mail import send_mail
from django.conf import settings

def test_email_configuration():
    """Test if email can be sent successfully."""
    
    print("=" * 70)
    print("EMAIL CONFIGURATION TEST")
    print("=" * 70)
    print()
    
    # Check configuration
    print("📋 Current Configuration:")
    print(f"   Backend: {settings.EMAIL_BACKEND}")
    print(f"   Host: {settings.EMAIL_HOST if hasattr(settings, 'EMAIL_HOST') else 'Not set'}")
    print(f"   Port: {settings.EMAIL_PORT if hasattr(settings, 'EMAIL_PORT') else 'Not set'}")
    print(f"   User: {settings.EMAIL_HOST_USER if hasattr(settings, 'EMAIL_HOST_USER') else 'Not set'}")
    print(f"   From: {settings.DEFAULT_FROM_EMAIL}")
    print()
    
    # Check if console backend
    if 'console' in settings.EMAIL_BACKEND.lower():
        print("⚠️  Console Backend Detected!")
        print()
        print("Emails will be printed to console, not sent to real email addresses.")
        print()
        print("To send real emails:")
        print("1. Run: python3 configure_email.py")
        print("2. Follow the setup instructions")
        print("3. Restart the server")
        print()
        return
    
    # Test sending
    print("🧪 Testing Email Sending...")
    print()
    
    test_email = input("Enter your email address to send a test: ").strip()
    
    if not test_email:
        print("❌ No email provided!")
        return
    
    try:
        print(f"📧 Sending test email to: {test_email}")
        print("   Please wait...")
        
        send_mail(
            subject='🔐 Test Email - AI Resume Builder',
            message='''
This is a test email from AI Resume Builder.

If you received this email, your password reset email configuration is working correctly! 🎉

You can now use the "Forgot Password" feature and receive real password reset links in your email inbox.

---
AI Resume Builder Team
            ''',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[test_email],
            fail_silently=False,
        )
        
        print()
        print("=" * 70)
        print("✅ EMAIL SENT SUCCESSFULLY!")
        print("=" * 70)
        print()
        print(f"📬 Check your inbox: {test_email}")
        print("   (Also check spam/junk folder)")
        print()
        print("If you received the email, your configuration is working!")
        print("You can now use the password reset feature with real emails.")
        print()
        
    except Exception as e:
        print()
        print("=" * 70)
        print("❌ EMAIL SENDING FAILED!")
        print("=" * 70)
        print()
        print(f"Error: {str(e)}")
        print()
        print("Common issues:")
        print()
        print("1. Gmail - App Password Required:")
        print("   ❌ Don't use your regular Gmail password")
        print("   ✅ Generate an App Password at:")
        print("      https://myaccount.google.com/apppasswords")
        print()
        print("2. Incorrect Credentials:")
        print("   - Double-check email and password")
        print("   - Run: python3 configure_email.py")
        print()
        print("3. Firewall/Network Issues:")
        print("   - Port 587 must be open")
        print("   - Try different network if blocked")
        print()
        print("4. 2-Factor Authentication:")
        print("   - Gmail requires App Password with 2FA")
        print("   - Enable 2FA first, then create App Password")
        print()

def show_setup_instructions():
    """Show quick setup instructions."""
    print("=" * 70)
    print("QUICK SETUP GUIDE")
    print("=" * 70)
    print()
    print("For Gmail (Recommended):")
    print()
    print("1. Enable 2-Factor Authentication:")
    print("   https://myaccount.google.com/security")
    print()
    print("2. Generate App Password:")
    print("   https://myaccount.google.com/apppasswords")
    print("   - Select: Mail")
    print("   - Select: Other (Custom name)")
    print("   - Name: Django Password Reset")
    print("   - Click: Generate")
    print("   - Copy the 16-character password")
    print()
    print("3. Run Configuration:")
    print("   python3 configure_email.py")
    print()
    print("4. Enter your Gmail and the App Password")
    print()
    print("5. Restart Django server")
    print()

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == '--help':
        show_setup_instructions()
    else:
        test_email_configuration()
