from django.contrib import admin

# Register your models here.
from django.contrib import admin
from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, loader.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)
