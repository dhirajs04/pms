# Generated by Django 4.0.5 on 2022-06-13 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0003_rolepermission_method'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rolepermission',
            old_name='path_name',
            new_name='app_name',
        ),
        migrations.RemoveField(
            model_name='rolepermission',
            name='method',
        ),
    ]
