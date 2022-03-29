from django.db import models
from django.contrib.auth.models import User


class Friendship(models.Model):
    
    class statusInvitation(models.TextChoices):
        PENDING = 'pending',
        FINISHED = 'finished'

    user_applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_applicant')
    user_receiving = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_receiving')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, choices=statusInvitation.choices, default=statusInvitation.PENDING)

    class Meta: 
        unique_together = (("user_applicant", "user_receiving"),)