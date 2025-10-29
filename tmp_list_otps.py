#!/usr/bin/env python3
"""List recent PasswordResetOTP entries from DB to verify OTPs are created."""
import os, django, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from users.models import PasswordResetOTP
from django.utils import timezone

print('Recent PasswordResetOTP entries:')
for otp in PasswordResetOTP.objects.all().order_by('-created_at')[:10]:
    print(otp.created_at.isoformat(), otp.user.email, otp.otp, 'used' if otp.is_used else 'unused')
