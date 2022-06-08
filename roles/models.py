from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        db_table = 'role'

    def __str__(self):
        return self.name
