from django.db import models


class Profile(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    gender = models.CharField(max_length=7)
    dob = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    mobile_no = models.EmailField(max_length=10, null=True, blank=True)
    profile_img = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='profile_created')
    updated_by = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='profile_updated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.first_name + " " + self.last_name
