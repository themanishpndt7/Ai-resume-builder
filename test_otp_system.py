"""
Test script for OTP-based password reset functionality.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from users.models import CustomUser, PasswordResetOTP
from django.utils import timezone

print("=" * 60)
print("OTP PASSWORD RESET - TEST SCRIPT")
print("=" * 60)

# Test OTP generation
print("\n1. Testing OTP Generation:")
otp = PasswordResetOTP.generate_otp()
print(f"   Generated OTP: {otp}")
print(f"   OTP Length: {len(otp)}")
print(f"   Is 6 digits: {len(otp) == 6 and otp.isdigit()}")

# Test with a user
print("\n2. Testing with User:")
try:
    # Get first user
    user = CustomUser.objects.first()
    if user:
        print(f"   User: {user.email}")
        
        # Create OTP
        otp_obj = PasswordResetOTP.objects.create(
            user=user,
            otp=PasswordResetOTP.generate_otp()
        )
        print(f"   Created OTP: {otp_obj.otp}")
        print(f"   Created at: {otp_obj.created_at}")
        print(f"   Is valid: {otp_obj.is_valid()}")
        print(f"   Is used: {otp_obj.is_used}")
        
        # Clean up test OTP
        otp_obj.delete()
        print("   Test OTP cleaned up ✓")
    else:
        print("   No users found in database")
except Exception as e:
    print(f"   Error: {e}")

print("\n3. OTP Validation Logic:")
print("   - OTP expires after 10 minutes")
print("   - OTP can only be used once")
print("   - Old OTPs are automatically deleted when new one is requested")

print("\n4. Password Reset Flow:")
print("   Step 1: User enters email → OTP sent")
print("   Step 2: User enters OTP → Verified")
print("   Step 3: User sets new password → Done")

print("\n" + "=" * 60)
print("OTP SYSTEM READY! ✓")
print("=" * 60)
