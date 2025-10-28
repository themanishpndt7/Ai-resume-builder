"""
Diagnostic view to test login page rendering
"""
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def test_login_diagnostic(request):
    """
    Test if login template can be rendered
    """
    try:
        # Try to render the login template
        context = {
            'form': None,  # Simplified test
        }
        return render(request, 'account/login.html', context)
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        return HttpResponse(f"""
            <h1>Error Details:</h1>
            <pre>{error_details}</pre>
            <hr>
            <h2>Exception: {str(e)}</h2>
        """, content_type="text/html", status=500)


def test_simple(request):
    """Simple test view"""
    return HttpResponse("""
        <h1>✅ Django is working!</h1>
        <p>If you see this, the server is responding.</p>
        <p><a href="/accounts/login/">Try Login Page</a></p>
    """)
