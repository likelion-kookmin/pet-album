from django.db import models
from account.models import CustomUser

# Create your models here.
class Pet_day(models.Model):
    customuser_id = models.ForeignKey#('CustomUser', on_delete=models.CASCADE)
    emoticon_01 = models.PositiveIntegerField(default=0)
    emoticon_02 = models.PositiveIntegerField(default=0)
    emoticon_03 = models.PositiveIntegerField(default=0)
    emoticon_04 = models.PositiveIntegerField(default=0)
    emoticon_05 = models.PositiveIntegerField(default=0)