from django.db import models


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        db_table = 'role'
        managed = False

    def __str__(self):
        return self.name
