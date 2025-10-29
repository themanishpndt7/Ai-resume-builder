#!/usr/bin/env python3
"""
Simple check for email environment variables
"""
import os
from pathlib import Path

# Load .env file
env_file = Path(__file__).parent / '.env'

print("\n" + "="*60)
print("EMAIL ENVIRONMENT VARIABLES CHECK")
print("="*60)

if env_file.exists():
    print(f"\n✅ .env file found: {env_file}")
    
    # Read .env file
    email_vars = {}
    with open(env_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('EMAIL_'):
                key, value = line.split('=', 1)
                email_vars[key] = value
    
    print("\n📧 Email variables in .env file:")
    for key, value in email_vars.items():
        if 'PASSWORD' in key:
            print(f"   {key} = {'*' * 10} (SET)")
        else:
            print(f"   {key} = {value}")
    
    if len(email_vars) >= 5:
        print("\n✅ All 5 email variables are set locally!")
    else:
        print(f"\n⚠️  Only {len(email_vars)}/5 email variables found")
else:
    print("\n❌ .env file NOT found!")

print("\n" + "="*60)
print("RENDER DEPLOYMENT STATUS")
print("="*60)

print("\n⚠️  IMPORTANT: The .env file is LOCAL only!")
print("    It is NOT deployed to Render (listed in .gitignore)")

print("\n📝 YOU MUST add these variables to Render Dashboard:")
print("\n   1. Go to: https://dashboard.render.com/")
print("   2. Select your service: ai-resume-builder-6jan")
print("   3. Click 'Environment' tab")
print("   4. Add these 5 variables:")
print("\n      EMAIL_HOST = smtp.gmail.com")
print("      EMAIL_PORT = 587")
print("      EMAIL_USE_TLS = True")
print("      EMAIL_HOST_USER = your-email@example.com")
print("      EMAIL_HOST_PASSWORD = <YOUR_APP_PASSWORD>")
print("\n   5. Click 'Save Changes'")
print("   6. Wait for automatic redeploy (2-3 minutes)")

print("\n" + "="*60)
print("VERIFICATION")
print("="*60)

print("\nAfter adding to Render, check the logs for:")
print("   ✅ 'Email configured: Real emails will be sent via SMTP'")
print("\nIf you see:")
print("   ❌ 'Email not configured: Emails will be printed to console'")
print("   → Variables are NOT set properly in Render")

print("\n" + "="*60 + "\n")
