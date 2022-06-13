from rest_framework.permissions import BasePermission

from roles.models import RolePermission, Role


class CanRead(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        role = Role.objects.get(user=user)
        app_name = request.resolver_match.app_names[0]
        return RolePermission.objects.filter(role=role, app_name=app_name, read=True)


class CanWrite(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        role = Role.objects.get(user=user)
        app_name = request.resolver_match.app_names[0]
        return RolePermission.objects.filter(role=role, app_name=app_name, write=True)


class CanUpdate(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        role = Role.objects.get(user=user)
        app_name = request.resolver_match.app_names[0]
        return RolePermission.objects.filter(role=role, app_name=app_name, update=True)


class CanDelete(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        role = Role.objects.get(user=user)
        app_name = request.resolver_match.app_names[0]
        return RolePermission.objects.filter(role=role, app_name=app_name, delete=True)
