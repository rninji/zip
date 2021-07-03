from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.
# class CustomUser(AbstractUser):
#     nickname=models.CharField(max_length=100)
#     first_name=models.CharField(max_length=100)
#     last_name=models.CharField(max_length=100)

class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname=models.CharField(max_length=64)
    profile_image=models.ImageField(blank=True)
    description=models.TextField(default='')
