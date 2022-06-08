from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

from roles.models import Role
from users.validators import UsernameValidator


class UserManager(BaseUserManager):
    def create_user(self, username, role, password=None):
        if not username:
            raise ValueError("Please Enter A Valid Username")

        user = self.model(
            username=username.strip(),
            role=role
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password):
        role = Role.objects.get(name='SuperAdmin')
        user = self.create_user(username, role, password)
        user.web_token = None
        user.mob_token = None
        user.is_mob_logged = False
        user.is_web_logged = False
        user.is_active = True
        user.is_verified = True
        user.save()
        return user


class User(AbstractBaseUser):
    username = models.CharField(
        max_length=120, unique=True,
        validators=[UsernameValidator()],
        error_messages={
            'unique': 'username already taken',
        },
    )

    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="user")
    web_token = models.CharField(max_length=255, null=True, blank=True)
    mob_token = models.CharField(max_length=255, null=True, blank=True)
    is_mob_logged = models.BooleanField(default=False)
    is_web_logged = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'

    def is_super_admin(self):
        return self.role == Role.objects.get(name='SuperAdmin')
