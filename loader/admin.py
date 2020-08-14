from django.contrib import admin

# Register your models here.
from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Item

class MyModelAdmin(AdminVideoMixin, loader.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)
