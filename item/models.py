from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Item(models.Model):
    TYPE_CHOICES={
        ('가구','가구'),
        ('패브릭','패브릭'),
        ('홈데코/조명','홈데코/조명'),
        ('DIY/공구','DIY/공구'),
        ('가전','가전'),
        ('수납/정리','수납/정리')
    }
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="post_items")
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='images/',blank=True)
    price=models.IntegerField(default=0)
    shop=models.URLField(default='')
    type=models.CharField(max_length=20,choices=TYPE_CHOICES)
    #like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_items", blank=True)


class ItemComment(models.Model):
    objects=models.Manager()
    # author=models.ForeignKey(User, on_delete=models.CASCADE)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item=models.ForeignKey('Item',on_delete=models.CASCADE)
    text=models.TextField(default='')
    created_date=models.DateTimeField(default=timezone.now)