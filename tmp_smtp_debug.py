#!/usr/bin/env python3
"""Direct smtplib session for SMTP debug with debuglevel=1.
This prints the SMTP dialogue to stdout so we can inspect server responses.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
import django
django.setup()
from django.conf import settings
import smtplib
from email.message import EmailMessage

host = getattr(settings, 'EMAIL_HOST', 'smtp.gmail.com')
port = int(getattr(settings, 'EMAIL_PORT', 587))
use_tls = getattr(settings, 'EMAIL_USE_TLS', True)
user = getattr(settings, 'EMAIL_HOST_USER', '')
password = getattr(settings, 'EMAIL_HOST_PASSWORD', '')
from_addr = getattr(settings, 'DEFAULT_FROM_EMAIL', user)

recipient = user or ''

print('SMTP debug to:', host, port)
print('User:', user)

msg = EmailMessage()
msg['Subject'] = '[AI Resume Builder] SMTP Raw Debug'
msg['From'] = from_addr
msg['To'] = recipient
msg.set_content('This is an SMTP debug message. If you see it, delivery worked.')

try:
    s = smtplib.SMTP(host, port, timeout=30)
    s.set_debuglevel(1)
    s.ehlo()
    if use_tls:
        s.starttls()
        s.ehlo()
    if user and password:
        s.login(user, password)
    s.send_message(msg)
    print('\nSMTP send_message succeeded (no exception).')
    s.quit()
except Exception as e:
    print('\nSMTP exception:')
    import traceback
    traceback.print_exc()
    print('\n--- end exception ---')
