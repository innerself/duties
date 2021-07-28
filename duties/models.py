from django.contrib.auth.models import User
from django.db import models

from duties.utils import random_color


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    color = models.CharField(max_length=20, default=random_color)

    def __str__(self):
        return f'Profile for user {self.user.username}'
