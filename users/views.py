from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserLoginSerializer


class UserLogin(APIView):

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            validate_data = serializer.validated_data

            data = {
                'token': validate_data.get('token')
            }

            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        if user:
            user.web_token = None
            user.save()
        return Response('Logged Out Successfully')
