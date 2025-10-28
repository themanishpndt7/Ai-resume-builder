from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import timedelta
import random


class CustomUser(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Uses email as the primary authentication field.
    Supports both email and username for flexibility.
    """
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # EMAIL as primary field but support username too
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    # Allow both email and username login
    def clean(self):
        super().clean()
        # Ensure username is unique
        if self.username:
            qs = CustomUser.objects.filter(username=self.username)
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            if qs.exists():
                raise ValueError(f"Username '{self.username}' is already taken.")
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.email


class SignupOTP(models.Model):
    """
    Model to store OTP for email verification during signup.
    OTP expires after 5 minutes for faster response.
    """
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)  # Hashed password
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Signup OTP'
        verbose_name_plural = 'Signup OTPs'
    
    def __str__(self):
        return f"Signup OTP for {self.email} - {self.otp}"
    
    def is_valid(self):
        """Check if OTP is still valid (not expired and not verified)."""
        if self.is_verified:
            return False
        expiry_time = self.created_at + timedelta(minutes=5)
        return timezone.now() < expiry_time
    
    @staticmethod
    def generate_otp():
        """Generate a random 6-digit OTP."""
        return str(random.randint(100000, 999999))


class PasswordResetOTP(models.Model):
    """
    Model to store OTP for password reset.
    OTP expires after 5 minutes for faster response.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='password_reset_otps')
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_used = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Password Reset OTP'
        verbose_name_plural = 'Password Reset OTPs'
    
    def __str__(self):
        return f"OTP for {self.user.email} - {self.otp}"
    
    def is_valid(self):
        """Check if OTP is still valid (not expired and not used)."""
        if self.is_used:
            return False
        expiry_time = self.created_at + timedelta(minutes=5)
        return timezone.now() < expiry_time
    
    @staticmethod
    def generate_otp():
        """Generate a random 6-digit OTP."""
        return str(random.randint(100000, 999999))
