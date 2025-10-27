"""
Diagnostic views to help debug production issues.
"""
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings
from users.models import CustomUser, PasswordResetOTP
import os


@require_http_methods(["GET"])
def config_check(request):
    """Check email and environment configuration (be careful with sensitive info!)"""
    
    config_info = {
        "email_backend": settings.EMAIL_BACKEND,
        "email_host": getattr(settings, 'EMAIL_HOST', 'Not set'),
        "email_port": getattr(settings, 'EMAIL_PORT', 'Not set'),
        "email_host_user_set": bool(getattr(settings, 'EMAIL_HOST_USER', '')),
        "email_password_set": bool(getattr(settings, 'EMAIL_HOST_PASSWORD', '')),
        "default_from_email": settings.DEFAULT_FROM_EMAIL,
        "email_use_tls": getattr(settings, 'EMAIL_USE_TLS', 'Not set'),
        "debug": settings.DEBUG,
        "allowed_hosts": settings.ALLOWED_HOSTS,
        "database_engine": settings.DATABASES['default']['ENGINE'],
    }
    
    return JsonResponse(config_info)


@require_http_methods(["GET"])
def test_email_quick(request):
    """Quick test to send an email"""
    from django.core.mail import send_mail
    
    try:
        send_mail(
            'Test Email from Render',
            'This is a test email to verify email configuration.',
            settings.DEFAULT_FROM_EMAIL,
            ['mpandat0052@gmail.com'],
            fail_silently=False,
        )
        return JsonResponse({
            "status": "success",
            "message": "Email sent successfully! Check your inbox."
        })
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)
