#!/usr/bin/env python3
"""
Quick script to POST to the password reset combined view using Django test client.
"""
import os, sys, django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from django.test import Client

client = Client()
email = 'test.user@example.com'
resp = client.post('/accounts/password/reset/', {'email': email, 'send_otp': '1'}, HTTP_HOST='localhost:8000')
print('STATUS:', resp.status_code)
print('REDIRECT:', resp.url if resp.status_code in (301,302) else '')
print('CONTENT SNIPPET:')
print(resp.content.decode('utf-8')[:1000])
