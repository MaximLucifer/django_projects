from django.contrib.auth.backends import BaseBackend
from .models import Client

class cliningAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Client.objects.get(username=username)
            if user.check_password(password):
                return user
        except Client.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Client.objects.get(pk=user_id)
        except Client.DoesNotExist:
            return None