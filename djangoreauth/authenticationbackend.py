from django.conf import settings
from django.contrib.auth.backends import RemoteUserBackend
from django.contrib.auth.models import User


class ReAuthBackend( RemoteUserBackend ):

    create_unknown_user = settings.REAUTH_CREATE_USERS

    def authenticate(self, reauth_username=None, *args, **kwargs):
        """
        Get or Add user if missing
        """
        user = None
        try:
            user = User.objects.get(username=reauth_username)
        except User.DoesNotExist:
            if self.create_unknown_user:
                user = User.objects.create(username=reauth_username)
        return user
