from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework import exceptions

User = get_user_model()


class PiAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('HTTP_X_HUBOLOGY_VIDEO_VILLAGE_PI')
        if not username:
            return None

        try:
            user = User.objects.get(username='pi')
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return user, True
