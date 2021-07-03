from django.contrib import admin
from .models import Item, ItemComment


# Register your models here.

admin.site.register(Item)
admin.site.register(ItemComment)
