#!/usr/bin/env python3
"""Send a non-interactive test email to the configured EMAIL_HOST_USER and print results."""
import os, django, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from django.conf import settings
from django.core.mail import send_mail

recipient = settings.EMAIL_HOST_USER or ''
print('Using backend:', settings.EMAIL_BACKEND)
print('Sending test email to:', recipient)
try:
    send_mail(
        subject='[AI Resume Builder] SMTP Deliverability Test',
        message='This is an automated SMTP deliverability test from the project workspace.',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[recipient],
        fail_silently=False,
    )
    print('Send call completed without exception. Check recipient inbox/spam.')
except Exception as e:
    print('Exception when sending email:')
    import traceback
    traceback.print_exc()
    print('\n--- End Exception ---')
