from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to="users/",
        blank=True,
        null=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    display_name = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )
    balance = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0
    )

    # social links
    instagram = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )
    telegram = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )
    facebook = models.CharField(
        max_length=256,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.username
