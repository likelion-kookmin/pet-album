from django.contrib import admin
from .models import Pet_day

# Register your models here.

class Pet_dayInline(admin.TabularInline):
    model = Pet_day

admin.site.register(Pet_day)