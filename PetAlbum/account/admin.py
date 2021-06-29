from django.contrib import admin
from .models import CustomUser
from django.utils.safestring import mark_safe
# Register your models here.

admin.site.register(CustomUser) #어드민에 유저 생김
class CustomUser(admin.ModelAdmin):
    list_display = ['photo_tag', 'nickname']

    list_display_links = ['name']

    def photo_tag(self, item):
        if item.image:
            return mark_safe('<img src={} style="width: 75px;"/>'.format(item.image.url))
        return None