# Generated by Django 4.0.3 on 2022-03-18 12:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friendship', '0002_friendship_create_time_friendship_update_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendship',
            old_name='id_user_applicant',
            new_name='user_applicant',
        ),
        migrations.RenameField(
            model_name='friendship',
            old_name='id_user_receiving',
            new_name='user_receiving',
        ),
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together={('user_applicant', 'user_receiving')},
        ),
    ]