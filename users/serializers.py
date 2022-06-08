import jwt
from django.contrib.auth import authenticate
from rest_framework import serializers

from pms import settings
from users.models import User


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):

        credentials = {
            'username': attrs.get('username'),
            'password': attrs.get('password')
        }

        if all(credentials.values()):
            try:
                user = User.objects.get(username=attrs.get('username'))
            except User.DoesNotExist:
                msg = 'Username / Password Wrong'
                raise serializers.ValidationError(msg)

            credentials['username'] = user.username

            user = authenticate(**credentials)

            if user:
                if not user.is_active:
                    raise serializers.ValidationError(
                        {'details': 'Your Account Is Not Active, Please Contact Admin'}
                    )

                payload = {
                    'id': user.pk,
                    'username': user.username,
                    'role': user.role
                }

                key = settings.SECRET_KEY

                token = jwt.encode(
                    payload,
                    key,
                ).decode('utf-8')

                user.web_token = token
                user.save()

                return {
                    'token': token,
                    'user': user
                }
            else:
                msg = 'Could not login with given credentials'
                raise serializers.ValidationError(msg)
        else:
            msg = "Please Provide username and password"
            raise serializers.ValidationError(msg)
