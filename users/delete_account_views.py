from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy, reverse
from django.views.generic import DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import transaction
from django.core.exceptions import PermissionDenied

from .models import CustomUser, DeletedEmail
from resume.models import Profile, Education, Experience, Project, GeneratedResume, CoverLetter

class AccountDeletionMixin:
    """Mixin to handle account deletion logic."""
    
    def delete_user_data(self, user):
        """
        Delete all user-related data.
        
        Args:
            user: The user whose data should be deleted
            
        Returns:
            str: The email of the deleted user
        """
        # Store the email before deletion
        email = user.email
        
        # Delete related data
        with transaction.atomic():
            # Store the email in deleted emails
            DeletedEmail.objects.create(
                email=email,
                deleted_at=timezone.now()
            )
            
            # Get the user's profile first (if exists)
            try:
                profile = Profile.objects.get(user=user)
                if profile.profile_photo:
                    profile.profile_photo.delete(save=False)
                profile.delete()
            except Profile.DoesNotExist:
                pass
                
            # Delete other related data
            Education.objects.filter(user=user).delete()
            Experience.objects.filter(user=user).delete()
            Project.objects.filter(user=user).delete()
            GeneratedResume.objects.filter(user=user).delete()
            CoverLetter.objects.filter(user=user).delete()
            
            # Delete the user
            user.delete()
        
        return email

@login_required
@require_POST
def delete_account(request):
    """
    View to delete the currently logged-in user's account.
    
    This view handles the POST request to delete a user's account and all associated data.
    The user is logged out after deletion, and the email is added to the DeletedEmail
    table to prevent immediate reuse.
    
    Args:
        request: The HTTP request object
        
    Returns:
        HttpResponseRedirect: Redirects to the home page with a success message
    """
    if not request.user.is_authenticated:
        raise PermissionDenied("You must be logged in to delete your account.")
    
    user = request.user
    email = user.email
    
    # Delete user data
    deletion_mixin = AccountDeletionMixin()
    deletion_mixin.delete_user_data(user)
    
    # Logout the user
    logout(request)
    
    messages.success(
        request, 
        _("Your account and all associated data have been permanently deleted. "
          "The email address %(email)s cannot be used to create a new account for 30 days.") % {'email': email}
    )
    return redirect('home')

class DeleteAccountView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    Class-based view for account deletion with confirmation.
    
    This view shows a confirmation page before deleting the user's account.
    On confirmation, it deletes all user data and prevents the email from being reused.
    """
    template_name = 'account/delete_account_confirm.html'
    success_url = reverse_lazy('home')
    success_message = _("Your account and all associated data have been permanently deleted.")
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        email = user.email
        
        # Delete user data
        deletion_mixin = AccountDeletionMixin()
        deletion_mixin.delete_user_data(user)
        
        # Logout the user
        logout(request)
        
        messages.success(
            self.request,
            _("Your account and all associated data have been permanently deleted. "
              "The email address %(email)s cannot be used to create a new account for 30 days.") % {'email': email}
        )
        return redirect(self.get_success_url())
