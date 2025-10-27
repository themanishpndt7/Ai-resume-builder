#!/usr/bin/env python3
"""
Quick Email Test - Verifies Gmail credentials work
"""

import smtplib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
EMAIL_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')

print("=" * 70)
print("GMAIL CREDENTIALS TEST")
print("=" * 70)
print()
print(f"📧 Email: {EMAIL_USER}")
print(f"🔐 Password: {'*' * len(EMAIL_PASSWORD)} ({len(EMAIL_PASSWORD)} chars)")
print(f"🌐 Host: {EMAIL_HOST}")
print(f"🔌 Port: {EMAIL_PORT}")
print()

if not EMAIL_USER or not EMAIL_PASSWORD:
    print("❌ Error: Email credentials not found in .env file")
    print()
    print("Please run: python3 configure_email.py")
    exit(1)

# Remove spaces from password if present
password_no_spaces = EMAIL_PASSWORD.replace(' ', '')

print("🧪 Testing SMTP connection...")
print()

try:
    # Connect to Gmail SMTP
    print("1. Connecting to smtp.gmail.com:587...")
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT, timeout=10)
    print("   ✅ Connected")
    
    print("2. Starting TLS...")
    server.starttls()
    print("   ✅ TLS started")
    
    print("3. Logging in...")
    print(f"   Email: {EMAIL_USER}")
    print(f"   Password: {'*' * len(password_no_spaces)} (without spaces)")
    
    # Try login with password without spaces
    server.login(EMAIL_USER, password_no_spaces)
    print("   ✅ Login successful!")
    
    server.quit()
    
    print()
    print("=" * 70)
    print("✅ SUCCESS! Gmail credentials are working!")
    print("=" * 70)
    print()
    print("Your email configuration is correct.")
    print()
    print("Next steps:")
    print("1. Make sure to RESTART your Django server")
    print("2. Try the password reset feature again")
    print()
    print("To restart server:")
    print("   Press Ctrl+C to stop current server")
    print("   python3 manage.py runserver")
    print()
    
except smtplib.SMTPAuthenticationError as e:
    print(f"   ❌ Authentication failed!")
    print()
    print("=" * 70)
    print("❌ AUTHENTICATION ERROR")
    print("=" * 70)
    print()
    print(f"Error: {e}")
    print()
    print("Possible issues:")
    print()
    print("1. App Password is incorrect")
    print("   - Go to: https://myaccount.google.com/apppasswords")
    print("   - Generate a NEW App Password")
    print("   - Copy it exactly (with or without spaces)")
    print()
    print("2. 2-Factor Authentication not enabled")
    print("   - Go to: https://myaccount.google.com/security")
    print("   - Enable 2-Step Verification")
    print("   - Then generate App Password")
    print()
    print("3. Using regular password instead of App Password")
    print("   - ❌ Don't use your Gmail password")
    print("   - ✅ Use 16-character App Password")
    print()
    print("To reconfigure:")
    print("   python3 configure_email.py")
    print()
    
except Exception as e:
    print(f"   ❌ Error: {e}")
    print()
    print("=" * 70)
    print("❌ CONNECTION ERROR")
    print("=" * 70)
    print()
    print(f"Error: {e}")
    print()
    print("Possible issues:")
    print("- Network/firewall blocking port 587")
    print("- SMTP server unreachable")
    print("- Incorrect host/port settings")
    print()

print()
