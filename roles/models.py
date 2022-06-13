from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        db_table = 'role'

    def __str__(self):
        return self.name


class RolePermission(models.Model):
    role = models.ForeignKey('Role', on_delete=models.CASCADE, related_name='role_permissions')
    app_name = models.CharField(max_length=100, unique=True)
    read = models.BooleanField(default=False)
    write = models.BooleanField(default=False)
    update = models.BooleanField(default=False)
    delete = models.BooleanField(default=False)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='role_permissions_created')
    updated_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='role_permissions_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'role_permission'

