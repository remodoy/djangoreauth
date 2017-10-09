from django.shortcuts import redirect
from django.views.decorators.csrf import requires_csrf_token
from django.conf import settings
from django.contrib.auth import login
import reauth
from .auth import reauth_authenticate_user


@requires_csrf_token
def reauth_login(request):
    if request.method == 'GET' and request.GET.get('code', None) is not None:
        code = request.GET.get('code')
        token = reauth.fetch_reauth_token(code, settings.REAUTH_URL)
        if token:
            user = reauth_authenticate_user(token)
            if user:
                request.user = user
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
    return redirect('login')
