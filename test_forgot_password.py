#!/usr/bin/env python3
"""
Test script for the Forgot Password feature.
This script demonstrates the password reset flow.
"""

import os
import sys
import django

# Setup Django environment
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

User = get_user_model()

def test_password_reset():
    """Test the password reset functionality."""
    print("=" * 60)
    print("FORGOT PASSWORD FEATURE - TEST SCRIPT")
    print("=" * 60)
    print()
    
    # Check if any users exist
    user_count = User.objects.count()
    print(f"📊 Total users in database: {user_count}")
    
    if user_count == 0:
        print("❌ No users found! Please create a test user first.")
        print("\nCreate a test user with:")
        print("  python3 manage.py createsuperuser")
        return
    
    print("\n✅ Users found in database:")
    for user in User.objects.all()[:5]:
        print(f"   - {user.email} (Username: {user.username})")
    
    print("\n" + "=" * 60)
    print("TESTING PASSWORD RESET FLOW")
    print("=" * 60)
    
    # Get a test user
    test_user = User.objects.first()
    print(f"\n🧪 Testing with user: {test_user.email}")
    
    # Generate reset token
    token = default_token_generator.make_token(test_user)
    uid = urlsafe_base64_encode(force_bytes(test_user.pk))
    
    print(f"\n🔐 Generated Reset Token:")
    print(f"   UID: {uid}")
    print(f"   Token: {token[:20]}...")
    
    # Construct reset URL
    reset_url = f"http://localhost:8000/accounts/password/reset/{uid}/{token}/"
    print(f"\n🔗 Reset URL:")
    print(f"   {reset_url}")
    
    print("\n" + "=" * 60)
    print("MANUAL TESTING STEPS")
    print("=" * 60)
    print("""
1. Start the development server:
   python3 manage.py runserver

2. Navigate to the login page:
   http://localhost:8000/accounts/login/

3. Click "Forgot password?" link

4. Enter a test email address:
   {}

5. Check the console/terminal for the reset email

6. Copy the reset link from the console output

7. Paste the link in your browser

8. Enter a new password and confirm

9. Verify you can login with the new password

    """.format(test_user.email))
    
    print("=" * 60)
    print("URL ENDPOINTS")
    print("=" * 60)
    print("""
Login Page:           /accounts/login/
Password Reset:       /accounts/password/reset/
Reset Done:           /accounts/password/reset/done/
Reset Confirm:        /accounts/password/reset/<uidb64>/<token>/
Reset Complete:       /accounts/password/reset/complete/
    """)
    
    print("=" * 60)
    print("EMAIL CONFIGURATION STATUS")
    print("=" * 60)
    
    from django.conf import settings
    print(f"\nEmail Backend: {settings.EMAIL_BACKEND}")
    print(f"Debug Mode: {settings.DEBUG}")
    
    if settings.DEBUG:
        print("\n✅ Development mode: Emails will be printed to console")
    else:
        print(f"\n📧 Production mode: Emails will be sent via SMTP")
        print(f"   Host: {settings.EMAIL_HOST}")
        print(f"   Port: {settings.EMAIL_PORT}")
        print(f"   From: {settings.DEFAULT_FROM_EMAIL}")
    
    print("\n" + "=" * 60)
    print("✅ TEST SCRIPT COMPLETE")
    print("=" * 60)

if __name__ == '__main__':
    test_password_reset()
