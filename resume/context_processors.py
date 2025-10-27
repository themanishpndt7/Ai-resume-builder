"""
Context processors for making variables available in all templates.
"""
from django.conf import settings


def theme(request):
    """
    Add theme information to template context.
    """
    current_theme = request.COOKIES.get(settings.THEME_COOKIE_NAME, settings.THEME_DEFAULT)
    return {
        'current_theme': current_theme,
    }
