#!/usr/bin/env python3
"""
Deployment Verification Script
Checks all critical settings for production deployment
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.conf import settings
from django.contrib.sessions.models import Session
from django.contrib.auth import get_user_model

User = get_user_model()

def check_mark(condition):
    return "✅" if condition else "❌"

def print_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def verify_settings():
    """Verify all critical Django settings"""
    print_section("DJANGO SETTINGS VERIFICATION")
    
    checks = {
        "DEBUG": settings.DEBUG,
        "SECRET_KEY set": bool(settings.SECRET_KEY and settings.SECRET_KEY != 'django-insecure-pu3b0yc&ibluwssn3k)x9l2h5!7d=oqq%8b%9d2ajb$wx_7oqg'),
        "ALLOWED_HOSTS configured": bool(settings.ALLOWED_HOSTS),
        "DATABASE configured": bool(settings.DATABASES),
    }
    
    for check, value in checks.items():
        print(f"{check_mark(value)} {check}: {value}")
    
    print(f"\n📋 ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    print(f"📋 RENDER_EXTERNAL_HOSTNAME: {os.getenv('RENDER_EXTERNAL_HOSTNAME', 'Not set')}")

def verify_session_config():
    """Verify session configuration"""
    print_section("SESSION CONFIGURATION")
    
    checks = {
        "SESSION_ENGINE": hasattr(settings, 'SESSION_ENGINE'),
        "SESSION_COOKIE_AGE": hasattr(settings, 'SESSION_COOKIE_AGE'),
        "SESSION_COOKIE_NAME": hasattr(settings, 'SESSION_COOKIE_NAME'),
        "SESSION_COOKIE_HTTPONLY": hasattr(settings, 'SESSION_COOKIE_HTTPONLY'),
        "SESSION_COOKIE_SAMESITE": hasattr(settings, 'SESSION_COOKIE_SAMESITE'),
    }
    
    for check, value in checks.items():
        status = check_mark(value)
        actual_value = getattr(settings, check, 'NOT SET')
        print(f"{status} {check}: {actual_value}")
    
    # Check session table
    try:
        session_count = Session.objects.count()
        print(f"\n✅ Session table accessible: {session_count} sessions in database")
    except Exception as e:
        print(f"\n❌ Session table error: {e}")

def verify_csrf_config():
    """Verify CSRF configuration"""
    print_section("CSRF CONFIGURATION")
    
    checks = {
        "CSRF_COOKIE_NAME": hasattr(settings, 'CSRF_COOKIE_NAME'),
        "CSRF_COOKIE_HTTPONLY": hasattr(settings, 'CSRF_COOKIE_HTTPONLY'),
        "CSRF_COOKIE_SAMESITE": hasattr(settings, 'CSRF_COOKIE_SAMESITE'),
        "CSRF_TRUSTED_ORIGINS": bool(settings.CSRF_TRUSTED_ORIGINS),
        "CSRF_FAILURE_VIEW": hasattr(settings, 'CSRF_FAILURE_VIEW'),
    }
    
    for check, value in checks.items():
        status = check_mark(value)
        actual_value = getattr(settings, check, 'NOT SET')
        print(f"{status} {check}: {actual_value}")
    
    print(f"\n📋 CSRF_TRUSTED_ORIGINS: {settings.CSRF_TRUSTED_ORIGINS}")

def verify_auth_config():
    """Verify authentication configuration"""
    print_section("AUTHENTICATION CONFIGURATION")
    
    checks = {
        "AUTH_USER_MODEL": hasattr(settings, 'AUTH_USER_MODEL'),
        "AUTHENTICATION_BACKENDS": bool(settings.AUTHENTICATION_BACKENDS),
        "LOGIN_REDIRECT_URL": hasattr(settings, 'LOGIN_REDIRECT_URL'),
        "LOGOUT_REDIRECT_URL": hasattr(settings, 'LOGOUT_REDIRECT_URL'),
        "LOGIN_URL": hasattr(settings, 'LOGIN_URL'),
    }
    
    for check, value in checks.items():
        status = check_mark(value)
        actual_value = getattr(settings, check, 'NOT SET')
        print(f"{status} {check}: {actual_value}")
    
    print(f"\n📋 AUTHENTICATION_BACKENDS:")
    for backend in settings.AUTHENTICATION_BACKENDS:
        print(f"   - {backend}")

def verify_security_settings():
    """Verify security settings for production"""
    print_section("SECURITY SETTINGS (Production)")
    
    if settings.DEBUG:
        print("⚠️  DEBUG=True - Security settings not enforced in development")
        return
    
    checks = {
        "SECURE_SSL_REDIRECT": getattr(settings, 'SECURE_SSL_REDIRECT', False),
        "SESSION_COOKIE_SECURE": getattr(settings, 'SESSION_COOKIE_SECURE', False),
        "CSRF_COOKIE_SECURE": getattr(settings, 'CSRF_COOKIE_SECURE', False),
        "SECURE_HSTS_SECONDS": getattr(settings, 'SECURE_HSTS_SECONDS', 0) > 0,
        "SECURE_PROXY_SSL_HEADER": hasattr(settings, 'SECURE_PROXY_SSL_HEADER'),
    }
    
    for check, value in checks.items():
        print(f"{check_mark(value)} {check}: {value}")

def verify_database():
    """Verify database connection and tables"""
    print_section("DATABASE VERIFICATION")
    
    try:
        # Check database connection
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        print("✅ Database connection: OK")
        
        # Check user table
        user_count = User.objects.count()
        print(f"✅ User table accessible: {user_count} users")
        
        # Check session table
        session_count = Session.objects.count()
        print(f"✅ Session table accessible: {session_count} sessions")
        
        # Check for active sessions
        from django.utils import timezone
        active_sessions = Session.objects.filter(expire_date__gt=timezone.now()).count()
        print(f"✅ Active sessions: {active_sessions}")
        
    except Exception as e:
        print(f"❌ Database error: {e}")

def verify_middleware():
    """Verify middleware configuration"""
    print_section("MIDDLEWARE CONFIGURATION")
    
    required_middleware = [
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'allauth.account.middleware.AccountMiddleware',
    ]
    
    for middleware in required_middleware:
        is_present = middleware in settings.MIDDLEWARE
        print(f"{check_mark(is_present)} {middleware}")

def verify_email_config():
    """Verify email configuration"""
    print_section("EMAIL CONFIGURATION")
    
    email_configured = bool(os.getenv('EMAIL_HOST_USER') and os.getenv('EMAIL_HOST_PASSWORD'))
    
    print(f"{check_mark(email_configured)} Email credentials configured")
    print(f"📋 EMAIL_BACKEND: {settings.EMAIL_BACKEND}")
    
    if email_configured:
        print(f"📋 EMAIL_HOST: {settings.EMAIL_HOST}")
        print(f"📋 EMAIL_PORT: {settings.EMAIL_PORT}")
        print(f"📋 EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}")
    else:
        print("⚠️  Email not configured - OTP emails will be printed to console")

def main():
    """Run all verification checks"""
    print("\n" + "="*60)
    print("  🔍 DEPLOYMENT VERIFICATION SCRIPT")
    print("  AI Resume Builder - Session & Login Fix")
    print("="*60)
    
    verify_settings()
    verify_session_config()
    verify_csrf_config()
    verify_auth_config()
    verify_security_settings()
    verify_middleware()
    verify_database()
    verify_email_config()
    
    print("\n" + "="*60)
    print("  ✅ VERIFICATION COMPLETE")
    print("="*60)
    
    if settings.DEBUG:
        print("\n⚠️  WARNING: DEBUG=True")
        print("   Set DEBUG=False for production deployment")
    else:
        print("\n✅ Production mode enabled (DEBUG=False)")
    
    print("\n📝 Next Steps:")
    print("   1. Review any ❌ items above")
    print("   2. Set missing environment variables")
    print("   3. Run: python manage.py migrate")
    print("   4. Deploy to Render")
    print("   5. Test login flow")
    
    print("\n" + "="*60 + "\n")

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"\n❌ Error running verification: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
