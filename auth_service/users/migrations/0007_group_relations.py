# Generated by Django 3.1.4 on 2021-05-10 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usergroup',
            name='admin',
        ),
        migrations.AddField(
            model_name='usergroup',
            name='admins',
            field=models.ManyToManyField(related_name='administrated_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='parent_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_groups', to='users.usergroup'),
        ),
    ]