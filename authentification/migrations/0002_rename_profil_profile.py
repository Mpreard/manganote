# Generated by Django 4.0.3 on 2022-03-25 09:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manganime', '0005_rename_profil_mangalibrairy_profile_and_more'),
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profil',
            new_name='Profile',
        ),
    ]