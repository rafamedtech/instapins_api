from django.contrib.auth.models import User
from .models import UserProfile

class EmailAuthBackend(object):
    """
    Authenticate using an e-mail address.
    """
    def authenticate(self, request, username=None, password=None):
        try:
            user = UserProfile.objects.get(username=username)
            if user.check_password(password):
                return user
            return None
        except UserProfile.DoesNotExist:
            return None
 
    def get_user(self, user_id):
        try:
            return UserProfile.objects.get(pk=user_id)
        except UserProfile.DoesNotExist:
            return None