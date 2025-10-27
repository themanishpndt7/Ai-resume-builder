"""
Custom password reset views using OTP instead of token links.
"""
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from users.models import CustomUser, PasswordResetOTP
from django import forms


class PasswordResetRequestForm(forms.Form):
    """Form to request password reset via email."""
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address'
        })
    )


class OTPVerificationForm(forms.Form):
    """Form to verify OTP."""
    email = forms.EmailField(widget=forms.HiddenInput())
    otp = forms.CharField(
        max_length=6,
        min_length=6,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter 6-digit OTP',
            'maxlength': '6'
        })
    )


class NewPasswordForm(forms.Form):
    """Form to set new password."""
    email = forms.EmailField(widget=forms.HiddenInput())
    otp = forms.CharField(max_length=6, widget=forms.HiddenInput())
    password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter new password'
        })
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm new password'
        })
    )
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match!")
        
        if password1 and len(password1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long!")
        
        return cleaned_data


class PasswordResetRequestView(View):
    """Step 1: User enters email to receive OTP."""
    template_name = 'account/password_reset.html'
    
    def get(self, request):
        form = PasswordResetRequestForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = PasswordResetRequestForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            
            try:
                user = CustomUser.objects.get(email=email, is_active=True)
                
                # Generate OTP
                otp_code = PasswordResetOTP.generate_otp()
                
                # Delete old unused OTPs for this user
                PasswordResetOTP.objects.filter(user=user, is_used=False).delete()
                
                # Create new OTP
                PasswordResetOTP.objects.create(user=user, otp=otp_code)
                
                # Send OTP via email
                subject = 'Password Reset OTP'
                message = f'''
Hello {user.get_full_name()},

You have requested to reset your password.

Your OTP code is: {otp_code}

This OTP is valid for 10 minutes.

If you did not request this, please ignore this email.

Best regards,
AI Resume Builder Team
                '''
                
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                
                messages.success(request, f'OTP has been sent to {email}. Please check your inbox.')
                return redirect('password_reset_verify_otp')
                
            except CustomUser.DoesNotExist:
                messages.error(request, 'No account found with this email address.')
                return render(request, self.template_name, {'form': form})
        
        return render(request, self.template_name, {'form': form})


class PasswordResetVerifyOTPView(View):
    """Step 2: User enters OTP to verify."""
    template_name = 'account/password_reset_verify_otp.html'
    
    def get(self, request):
        form = OTPVerificationForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = OTPVerificationForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            otp = form.cleaned_data['otp']
            
            try:
                user = CustomUser.objects.get(email=email, is_active=True)
                otp_obj = PasswordResetOTP.objects.filter(
                    user=user,
                    otp=otp,
                    is_used=False
                ).order_by('-created_at').first()
                
                if otp_obj and otp_obj.is_valid():
                    # OTP is valid, proceed to password reset
                    request.session['reset_email'] = email
                    request.session['reset_otp'] = otp
                    messages.success(request, 'OTP verified successfully! Please set your new password.')
                    return redirect('password_reset_confirm')
                else:
                    messages.error(request, 'Invalid or expired OTP. Please try again.')
                    
            except CustomUser.DoesNotExist:
                messages.error(request, 'Invalid email address.')
        
        return render(request, self.template_name, {'form': form})


class PasswordResetConfirmView(View):
    """Step 3: User sets new password after OTP verification."""
    template_name = 'account/password_reset_confirm.html'
    
    def get(self, request):
        # Check if user has verified OTP
        if 'reset_email' not in request.session or 'reset_otp' not in request.session:
            messages.error(request, 'Please verify OTP first.')
            return redirect('password_reset_verify_otp')
        
        form = NewPasswordForm(initial={
            'email': request.session.get('reset_email'),
            'otp': request.session.get('reset_otp')
        })
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = NewPasswordForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            otp = form.cleaned_data['otp']
            password = form.cleaned_data['password1']
            
            try:
                user = CustomUser.objects.get(email=email, is_active=True)
                otp_obj = PasswordResetOTP.objects.filter(
                    user=user,
                    otp=otp,
                    is_used=False
                ).order_by('-created_at').first()
                
                if otp_obj and otp_obj.is_valid():
                    # Set new password
                    user.set_password(password)
                    user.save()
                    
                    # Mark OTP as used
                    otp_obj.is_used = True
                    otp_obj.save()
                    
                    # Clear session
                    request.session.pop('reset_email', None)
                    request.session.pop('reset_otp', None)
                    
                    messages.success(request, 'Your password has been reset successfully! You can now login.')
                    return redirect('password_reset_complete')
                else:
                    messages.error(request, 'Invalid or expired OTP.')
                    return redirect('password_reset_request')
                    
            except CustomUser.DoesNotExist:
                messages.error(request, 'Invalid user.')
                return redirect('password_reset_request')
        
        return render(request, self.template_name, {'form': form})


class PasswordResetCompleteView(View):
    """Step 4: Show success message."""
    template_name = 'account/password_reset_complete.html'
    
    def get(self, request):
        return render(request, self.template_name)
