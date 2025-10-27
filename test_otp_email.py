"""
Quick test to demonstrate OTP email sending.
Run this after requesting password reset on the website.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from users.models import CustomUser, PasswordResetOTP
from django.core.mail import send_mail
from django.conf import settings

print("=" * 70)
print("OTP PASSWORD RESET - MANUAL TEST")
print("=" * 70)

# Get a user to test with
user = CustomUser.objects.first()

if user:
    print(f"\n✓ Testing with user: {user.email}")
    
    # Generate OTP
    otp_code = PasswordResetOTP.generate_otp()
    print(f"✓ Generated OTP: {otp_code}")
    
    # Delete old OTPs
    old_count = PasswordResetOTP.objects.filter(user=user, is_used=False).count()
    PasswordResetOTP.objects.filter(user=user, is_used=False).delete()
    print(f"✓ Deleted {old_count} old OTP(s)")
    
    # Create new OTP
    otp_obj = PasswordResetOTP.objects.create(user=user, otp=otp_code)
    print(f"✓ Created new OTP in database")
    
    # Send email
    subject = 'Password Reset OTP - TEST'
    message = f'''
Hello {user.get_full_name()},

This is a TEST email for the OTP password reset system.

Your OTP code is: {otp_code}

This OTP is valid for 10 minutes.

If you did not request this, please ignore this email.

Best regards,
AI Resume Builder Team
    '''
    
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        print(f"✓ Email sent successfully to {user.email}")
        print(f"\n" + "=" * 70)
        print("CHECK YOUR EMAIL FOR THE OTP CODE!")
        print("=" * 70)
        print(f"\nOTP CODE (also in email): {otp_code}")
        print(f"Valid for: 10 minutes")
        print(f"Expires at: {otp_obj.created_at.strftime('%H:%M:%S')} + 10 minutes")
        
    except Exception as e:
        print(f"✗ Error sending email: {e}")
    
    # Clean up test OTP
    print(f"\nℹ Test OTP will remain in database for testing.")
    print(f"  To clean up, run: PasswordResetOTP.objects.filter(user__email='{user.email}').delete()")
    
else:
    print("\n✗ No users found in database!")
    print("  Create a user first in Django admin or via signup")

print("\n" + "=" * 70)
