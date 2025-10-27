#!/usr/bin/env python
import os
import django
from django.contrib.auth import get_user_model

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

User = get_user_model()

# Create superuser with specified credentials
username = 'admin'
email = 'mpandat0052@gmail.com'
password = '123456'

# Check if user already exists
if User.objects.filter(username=username).exists():
    print(f"✓ Superuser '{username}' already exists!")
    user = User.objects.get(username=username)
    # Update password and permissions
    user.set_password(password)
    # Only update email if it's different and not already taken
    if user.email != email:
        # Check if another user has this email
        if User.objects.filter(email=email).exclude(id=user.id).exists():
            print(f"⚠ Email {email} is already in use by another account")
            print(f"  Keeping existing email: {user.email}")
        else:
            user.email = email
            print(f"✓ Email updated to: {email}")
    user.is_staff = True
    user.is_superuser = True
    user.is_active = True
    user.save()
    print(f"✓ Password updated to: {password}")
    print(f"✓ Staff permissions enabled: True")
    print(f"✓ Superuser permissions enabled: True")
else:
    # Create new superuser
    user = User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print(f"✓ Superuser '{username}' created successfully!")
    print(f"✓ Email: {email}")
    print(f"✓ Password: {password}")

print("\n✅ Superuser setup complete!")
print(f"You can now login at: http://127.0.0.1:8000/admin/")
print(f"Username: {username}")
print(f"Password: {password}")
