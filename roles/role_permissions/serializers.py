from rest_framework import serializers

from roles.models import RolePermission
from roles.serializers import RoleSerializer


class RolePermissionsSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = RolePermission
        fields = [
            'id',
            'role',
            'app_name',
            'read',
            'write',
            'update',
            'delete'
        ]
