from django.contrib import admin
from .models import CustomUser
from django.utils.safestring import mark_safe
# from my_pet.admin import Pet_dayInline
# from my_pet.models import Pet_day
# Register your models here.

admin.site.register(CustomUser) #어드민에 유저 생김
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['photo_tag', 'nickname']

    list_display_links = ['name']

    # inlines = [
    #     Pet_dayInline,
    # ]

    def photo_tag(self, item):
        if item.image:
            return mark_safe('<img src={} style="width: 75px;"/>'.format(item.image.url))
        return None