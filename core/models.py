from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, verbose_name="شماره تلفن")
    address = models.TextField(blank=True, verbose_name="آدرس")

    def __str__(self):
        return self.username
