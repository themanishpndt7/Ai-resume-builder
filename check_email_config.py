#!/usr/bin/env python3
"""
Check Django Email Configuration
Shows what Django is actually using vs what's in .env
"""

import os
import sys
import django
from dotenv import load_dotenv

# Load .env first
load_dotenv()

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.conf import settings

print("=" * 70)
print("EMAIL CONFIGURATION CHECK")
print("=" * 70)
print()

# What's in .env
print("📄 FROM .ENV FILE:")
env_user = os.getenv('EMAIL_HOST_USER', 'NOT SET')
env_password = os.getenv('EMAIL_HOST_PASSWORD', 'NOT SET')
print(f"   EMAIL_HOST_USER: {env_user}")
print(f"   EMAIL_HOST_PASSWORD: {'*' * len(env_password) if env_password != 'NOT SET' else 'NOT SET'}")
print()

# What Django is using
print("⚙️  DJANGO SETTINGS (What's actually being used):")
django_user = settings.EMAIL_HOST_USER if hasattr(settings, 'EMAIL_HOST_USER') else 'NOT SET'
django_password = settings.EMAIL_HOST_PASSWORD if hasattr(settings, 'EMAIL_HOST_PASSWORD') else 'NOT SET'
django_backend = settings.EMAIL_BACKEND if hasattr(settings, 'EMAIL_BACKEND') else 'NOT SET'

print(f"   EMAIL_BACKEND: {django_backend}")
print(f"   EMAIL_HOST_USER: {django_user}")
print(f"   EMAIL_HOST_PASSWORD: {'*' * len(django_password) if django_password != 'NOT SET' else 'NOT SET'}")
print()

# Check if they match
print("=" * 70)
if env_user == django_user:
    print("✅ CONFIGURATION MATCHES!")
    print()
    print("Django is using the correct email from .env file.")
    print()
    if django_user == 'mpandat0052@gmail.com':
        print("✅ Correct email: mpandat0052@gmail.com")
        print()
        print("Your password reset emails should work now!")
        print()
        print("Test it at: http://localhost:8000/accounts/login/")
    else:
        print(f"⚠️  Email is: {django_user}")
        print("   (Make sure this is correct)")
else:
    print("❌ CONFIGURATION MISMATCH!")
    print()
    print(f"   .env has: {env_user}")
    print(f"   Django using: {django_user}")
    print()
    print("⚠️  Django is NOT using the .env configuration!")
    print()
    print("SOLUTION: Restart the Django server")
    print()
    print("   ./restart_server.sh")
    print()
    print("Or manually:")
    print("   1. Press Ctrl+C to stop server")
    print("   2. python3 manage.py runserver")

print("=" * 70)
print()
