"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from resume.password_reset_views import (
    PasswordResetRequestView,
    PasswordResetVerifyOTPView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Custom OTP-based password reset (must be before allauth)
    path('accounts/password/reset/', PasswordResetRequestView.as_view(), name='account_reset_password'),
    path('accounts/password/reset/verify/', PasswordResetVerifyOTPView.as_view(), name='password_reset_verify_otp'),
    path('accounts/password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password/reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    # Allauth URLs (our custom password reset will override)
    path('accounts/', include('allauth.urls')),
    
    # Resume app URLs
    path('', include('resume.urls')),
]

# Serve media files in both development and production
# For production: Consider using cloud storage (AWS S3, Cloudinary, etc.) for persistent storage
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files only in development (WhiteNoise handles in production)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
