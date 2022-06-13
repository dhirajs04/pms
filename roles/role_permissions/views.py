from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from roles.models import RolePermission
from roles.role_permissions.serializers import RolePermissionsSerializer
from users.permissions import CanRead


class RolePermissionsListView(generics.GenericAPIView):

    permission_classes = [IsAuthenticated, CanRead]

    def get_queryset(self):
        role_permission_list = RolePermission.objects.all()
        return role_permission_list

    def get_serializer_class(self):
        return RolePermissionsSerializer

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RolePermissionDetailView(APIView):

    permission_classes = [IsAuthenticated, CanRead]

    def get_object(self, pk):
        try:
            role_permission = RolePermission.objects.get(pk=pk)
        except RolePermission.DoesNotExist:
            raise NotFound(detail='RolePermission Not Found')
        return role_permission

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = RolePermissionsSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
