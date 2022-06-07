from rest_framework import serializers

from roles.models import Role


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = [
            'role_id',
            'name'
        ]


class RoleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = [
            'name'
        ]


class RoleEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = [
            'role_id',
            'name'
        ]
