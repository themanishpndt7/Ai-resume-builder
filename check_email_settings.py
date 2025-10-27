#!/usr/bin/env python
"""
Check if email settings are properly configured
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.conf import settings
from django.core.mail import send_mail

print("\n" + "="*60)
print("EMAIL CONFIGURATION CHECK")
print("="*60)

print(f"\n📧 EMAIL_BACKEND: {settings.EMAIL_BACKEND}")
print(f"📧 EMAIL_HOST: {getattr(settings, 'EMAIL_HOST', 'Not set')}")
print(f"📧 EMAIL_PORT: {getattr(settings, 'EMAIL_PORT', 'Not set')}")
print(f"📧 EMAIL_USE_TLS: {getattr(settings, 'EMAIL_USE_TLS', 'Not set')}")
print(f"📧 EMAIL_HOST_USER: {settings.EMAIL_HOST_USER if settings.EMAIL_HOST_USER else '❌ NOT SET'}")
print(f"📧 EMAIL_HOST_PASSWORD: {'✅ SET' if settings.EMAIL_HOST_PASSWORD else '❌ NOT SET'}")
print(f"📧 DEFAULT_FROM_EMAIL: {settings.DEFAULT_FROM_EMAIL}")

print("\n" + "="*60)

if settings.EMAIL_HOST_USER and settings.EMAIL_HOST_PASSWORD:
    print("✅ Email credentials are configured!")
    print("\nAttempting to send test email...")
    
    try:
        send_mail(
            subject='Test Email from AI Resume Builder',
            message='This is a test email to verify SMTP configuration.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        print("✅ Test email sent successfully!")
        print(f"   Check inbox: {settings.EMAIL_HOST_USER}")
    except Exception as e:
        print(f"❌ Failed to send email:")
        print(f"   Error: {str(e)}")
else:
    print("❌ Email credentials NOT configured!")
    print("\n📝 Required environment variables:")
    print("   - EMAIL_HOST_USER")
    print("   - EMAIL_HOST_PASSWORD")
    print("\n💡 Set these in Render Dashboard → Environment Variables")

print("="*60 + "\n")
