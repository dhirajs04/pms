import jwt
from rest_framework import authentication, exceptions

from pms import settings
from users.models import User


class CustomJWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)

        if not auth_data:
            return None

        token = auth_data.decode('utf-8').split(' ')[1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

            user = User.objects.get(username=payload['username'])
            if user:
                if user.web_token == token:
                    return user, token

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Token Expired')
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed('Invalid Token,')
