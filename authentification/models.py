from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=12, null=True)
    picture = models.BinaryField(null=True)

    @receiver(post_save, sender=User)  # add this
    def create_user_profil(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)  # add this
    def save_user_profil(sender, instance, **kwargs):
        instance.profile.save()
