from django.contrib import admin
from .models import Notice
from .models import Cs
from .models import Cs_comment

# Register your models here.
admin.site.register(Notice)
admin.site.register(Cs)
admin.site.register(Cs_comment)