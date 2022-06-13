from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from roles.models import Role
from roles.serializers import RoleSerializer, RoleCreateSerializer, RoleEditSerializer
from users.permissions import CanRead, CanWrite, CanUpdate


class RoleListView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated, CanRead]

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
    permission_classes = [IsAuthenticated, CanRead]

    def get_object(self, pk):
        try:
            role = Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            raise NotFound(detail='Role Not Found')
        return role

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = RoleSerializer(queryset)
        return Response(serializer.data)


class RoleCreateView(APIView):
    permission_classes = [IsAuthenticated, CanWrite]

    def post(self, request):
        serializer = RoleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleEditView(APIView):

    permission_classes = [IsAuthenticated, CanUpdate]

    def put(self, request, pk):
        try:
            role = Role.objects.get(pk=pk)
        except Role.DoesNotExist:
            raise NotFound(detail='Role Not Found')
        serializer = RoleEditSerializer(instance=role, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
