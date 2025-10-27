from django import forms
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from .models import CustomUser
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from resume.countries_data import PHONE_CODES as PHONE_CODE_CHOICES


class CustomSignupForm(SignupForm):
    """
    Custom signup form for django-allauth.
    """
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )
    
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class UserProfileForm(forms.ModelForm):
    """
    Form for updating user profile information.
    """
    phone_country_code = forms.ChoiceField(
        choices=PHONE_CODE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone', 'profile_photo']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number (without country code)'}),
            'profile_photo': forms.FileInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Extract country code from phone if it exists
        if self.instance and self.instance.phone:
            phone = self.instance.phone
            for code, label in PHONE_CODE_CHOICES[1:]:  # Skip empty choice
                if phone.startswith(code):
                    self.initial['phone_country_code'] = code
                    self.initial['phone'] = phone[len(code):].strip()
                    break
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        # Combine country code with phone number
        country_code = self.cleaned_data.get('phone_country_code', '')
        phone = self.cleaned_data.get('phone', '')
        if country_code and phone:
            instance.phone = f"{country_code} {phone}"
        elif phone:
            instance.phone = phone
        if commit:
            instance.save()
        return instance
