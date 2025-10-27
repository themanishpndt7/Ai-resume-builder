"""
Custom allauth adapter to disable default password reset.
"""
from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    """
    Custom adapter to use OTP-based password reset instead of allauth's default.
    """
    
    def send_mail(self, template_prefix, email, context):
        """
        Override to prevent allauth from sending password reset emails.
        Our custom OTP system handles password resets.
        """
        # Only block password reset emails, allow other emails
        if template_prefix == 'account/email/password_reset_key':
            # Don't send allauth password reset email
            return
        
        # Allow other emails (verification, etc.)
        super().send_mail(template_prefix, email, context)
