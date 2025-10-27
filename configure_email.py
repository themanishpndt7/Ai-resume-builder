#!/usr/bin/env python3
"""
Email Configuration Helper for Password Reset Feature

This script helps you configure email settings to send real password reset emails.
"""

import os
from pathlib import Path

def create_env_file():
    """Create or update .env file with email configuration."""
    
    print("=" * 70)
    print("EMAIL CONFIGURATION FOR PASSWORD RESET")
    print("=" * 70)
    print()
    print("This will configure your application to send REAL password reset emails.")
    print()
    
    # Check if .env exists
    env_file = Path('.env')
    existing_config = {}
    
    if env_file.exists():
        print("📄 Found existing .env file")
        with open(env_file, 'r') as f:
            for line in f:
                if '=' in line and not line.strip().startswith('#'):
                    key, value = line.strip().split('=', 1)
                    existing_config[key] = value
        print()
    
    print("Choose your email provider:")
    print("1. Gmail (recommended for testing)")
    print("2. Outlook/Hotmail")
    print("3. Yahoo")
    print("4. Custom SMTP")
    print()
    
    choice = input("Enter choice (1-4): ").strip()
    
    # Email provider settings
    providers = {
        '1': {
            'name': 'Gmail',
            'host': 'smtp.gmail.com',
            'port': '587',
            'instructions': '''
📧 GMAIL SETUP INSTRUCTIONS:

1. Enable 2-Factor Authentication:
   - Go to: https://myaccount.google.com/security
   - Enable "2-Step Verification"

2. Generate App Password:
   - Go to: https://myaccount.google.com/apppasswords
   - Select: Mail → Other (Custom name)
   - Name it: "Django Password Reset"
   - Click "Generate"
   - Copy the 16-character password

3. Use the App Password (not your regular Gmail password)

⚠️  IMPORTANT: You MUST use an App Password, not your regular password!
'''
        },
        '2': {
            'name': 'Outlook',
            'host': 'smtp-mail.outlook.com',
            'port': '587',
            'instructions': '''
📧 OUTLOOK SETUP INSTRUCTIONS:

1. Use your Outlook/Hotmail email and password
2. Make sure "Less secure app access" is enabled if needed
3. Port: 587
4. TLS: Yes
'''
        },
        '3': {
            'name': 'Yahoo',
            'host': 'smtp.mail.yahoo.com',
            'port': '587',
            'instructions': '''
📧 YAHOO SETUP INSTRUCTIONS:

1. Generate App Password:
   - Go to: https://login.yahoo.com/account/security
   - Enable "Allow apps that use less secure sign in"
   - Generate an app password

2. Use the App Password (not your regular Yahoo password)
'''
        },
        '4': {
            'name': 'Custom',
            'host': '',
            'port': '587',
            'instructions': 'Enter your custom SMTP settings below.'
        }
    }
    
    if choice not in providers:
        print("❌ Invalid choice!")
        return
    
    provider = providers[choice]
    print()
    print(provider['instructions'])
    print()
    
    # Get configuration
    print("-" * 70)
    print("ENTER YOUR EMAIL CREDENTIALS:")
    print("-" * 70)
    
    if choice == '4':
        email_host = input("SMTP Host (e.g., smtp.example.com): ").strip()
        email_port = input("SMTP Port (default 587): ").strip() or '587'
    else:
        email_host = provider['host']
        email_port = provider['port']
        print(f"✅ SMTP Host: {email_host}")
        print(f"✅ SMTP Port: {email_port}")
        print()
    
    email_user = input("Your Email Address: ").strip()
    
    if not email_user:
        print("❌ Email address is required!")
        return
    
    import getpass
    email_password = getpass.getpass("Email Password (App Password for Gmail): ").strip()
    
    if not email_password:
        print("❌ Password is required!")
        return
    
    email_use_tls = input("Use TLS? (Y/n): ").strip().lower() or 'y'
    
    # Create .env content
    env_content = []
    
    # Preserve existing non-email settings
    for key, value in existing_config.items():
        if not key.startswith('EMAIL_') and key not in ['DEFAULT_FROM_EMAIL', 'SERVER_EMAIL']:
            env_content.append(f"{key}={value}")
    
    # Add email settings
    env_content.extend([
        "",
        "# Email Configuration for Password Reset",
        f"EMAIL_HOST={email_host}",
        f"EMAIL_PORT={email_port}",
        f"EMAIL_USE_TLS={'True' if email_use_tls == 'y' else 'False'}",
        f"EMAIL_HOST_USER={email_user}",
        f"EMAIL_HOST_PASSWORD={email_password}",
        f"DEFAULT_FROM_EMAIL={email_user}",
        f"SERVER_EMAIL={email_user}",
        ""
    ])
    
    # Write to .env file
    with open(env_file, 'w') as f:
        f.write('\n'.join(env_content))
    
    # Make sure .env is in .gitignore
    gitignore_file = Path('.gitignore')
    if gitignore_file.exists():
        with open(gitignore_file, 'r') as f:
            gitignore_content = f.read()
        
        if '.env' not in gitignore_content:
            with open(gitignore_file, 'a') as f:
                f.write('\n# Environment variables\n.env\n*.env\n')
    else:
        with open(gitignore_file, 'w') as f:
            f.write('# Environment variables\n.env\n*.env\n')
    
    print()
    print("=" * 70)
    print("✅ EMAIL CONFIGURATION SAVED!")
    print("=" * 70)
    print()
    print("📄 Configuration saved to: .env")
    print("🔒 .env added to .gitignore for security")
    print()
    print("Next steps:")
    print("1. Restart your Django server")
    print("2. Test the password reset feature")
    print("3. Check your email inbox for the reset link")
    print()
    print("To test email sending, run:")
    print("  python3 test_email_sending.py")
    print()

def show_current_config():
    """Show current email configuration."""
    env_file = Path('.env')
    
    if not env_file.exists():
        print("❌ No .env file found. Email not configured.")
        return
    
    print("=" * 70)
    print("CURRENT EMAIL CONFIGURATION")
    print("=" * 70)
    
    with open(env_file, 'r') as f:
        for line in f:
            if line.strip() and not line.strip().startswith('#'):
                if 'EMAIL' in line or 'FROM_EMAIL' in line:
                    key, value = line.strip().split('=', 1)
                    # Hide password
                    if 'PASSWORD' in key:
                        value = '*' * len(value)
                    print(f"{key}: {value}")
    print()

if __name__ == '__main__':
    print()
    print("Choose an option:")
    print("1. Configure email settings")
    print("2. Show current configuration")
    print("3. Exit")
    print()
    
    option = input("Enter choice (1-3): ").strip()
    
    if option == '1':
        create_env_file()
    elif option == '2':
        show_current_config()
    else:
        print("Goodbye!")
