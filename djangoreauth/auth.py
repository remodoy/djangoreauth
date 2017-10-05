from django.contrib.auth import authenticate
from django.conf import settings
import reauth


def reauth_authenticate_user(token):
    """
    Authenticate user by ReAuth token
    :param token:
    :return:
    """
    public_key = getattr(settings, 'REAUTH_PUBLIC_KEY', None)
    if not public_key:
        public_key = reauth.get_public_key(settings.REAUTH_URL)
    if not public_key:
        return
    claims = reauth.decode_reauth_token(token, public_key=public_key)
    if claims:
        return authenticate(reauth_username=claims['username'])
    return None
