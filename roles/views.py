from rest_framework import generics, status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from roles.models import Role
from roles.serializers import RoleSerializer


class RoleListView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        role_list = Role.objects.all()
        return role_list

    def get_serializer_class(self):
        return RoleSerializer

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RoleDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return Role.objects.get(pk=pk)
        # try:
        #     role = Role.objects.get(pk=pk)
        # except Role.DoesNotExist:
        #     return serializers.ValidationError({'details': 'Role Not Found'})
        # return role

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = RoleSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
