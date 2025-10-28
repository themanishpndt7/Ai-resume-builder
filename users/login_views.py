"""
Custom login view to handle 'Remember me' functionality and prevent 500 errors.
"""
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from allauth.account.views import LoginView as AllauthLoginView
from allauth.account.utils import perform_login
from allauth.exceptions import ImmediateHttpResponse
import logging

logger = logging.getLogger(__name__)


class CustomLoginView(AllauthLoginView):
    """
    Custom login view that extends allauth's LoginView to handle:
    - 'Remember me' checkbox for session persistence
    - Graceful error handling to prevent 500 errors
    - Proper session expiry management
    """
    
    def form_valid(self, form):
        """
        Handle successful form validation.
        Override to add 'Remember me' functionality and welcome message.
        """
        try:
            # Get the 'remember' checkbox value
            remember_me = self.request.POST.get('remember', None)
            
            # Set session expiry based on 'remember me' checkbox
            if remember_me:
                # Remember for 2 weeks (1209600 seconds)
                self.request.session.set_expiry(1209600)
                logger.info("Session set to persist for 2 weeks (Remember me enabled)")
            else:
                # Expire when browser closes (0 = browser-length session)
                self.request.session.set_expiry(0)
                logger.info("Session set to expire on browser close (Remember me disabled)")
            
            # Call parent's form_valid which handles the actual login
            response = super().form_valid(form)
            
            # Add welcome message after successful login
            user = self.request.user
            if user.is_authenticated:
                messages.success(
                    self.request,
                    f'Welcome back, {user.get_full_name()}! 🎉'
                )
                logger.info(f"✅ User logged in successfully: {user.email}")
            
            return response
            
        except ImmediateHttpResponse:
            # Re-raise allauth's redirect exceptions
            raise
        except Exception as e:
            # Log the error and show user-friendly message
            logger.exception(f"Login error: {str(e)}")
            messages.error(
                self.request,
                'An error occurred during login. Please try again or contact support if the issue persists.'
            )
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        """
        Handle form validation errors gracefully.
        """
        try:
            # Log form errors for debugging
            if form.errors:
                logger.warning(f"Login form validation errors: {form.errors}")
            
            return super().form_invalid(form)
            
        except Exception as e:
            # Catch any unexpected errors in form rendering
            logger.exception(f"Error rendering login form: {str(e)}")
            messages.error(
                self.request,
                'An error occurred. Please try again.'
            )
            return render(self.request, self.template_name, {'form': form})
    
    def get(self, request, *args, **kwargs):
        """
        Handle GET requests gracefully.
        """
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            logger.exception(f"Error loading login page: {str(e)}")
            messages.error(
                request,
                'An error occurred loading the login page. Please refresh and try again.'
            )
            # Return a basic login form even if there's an error
            from allauth.account.forms import LoginForm
            form = LoginForm()
            return render(request, self.template_name, {'form': form})
