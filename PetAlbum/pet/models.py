from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import related


class Pet_page(models.Model):
    # user_id = models.ForeignKey
    user_id = models.IntegerField()
    title = models.CharField(max_length=50)


# Create your models here.
class Pet(models.Model):
    # user_id = models.ForeignKey
    user_id = models.IntegerField()
    pet_page_id = models.ForeignKey(Pet_page, on_delete=CASCADE, related_name='pets')
    pet_image = models.ImageField()
    name = models.CharField(max_length=30)
    birthday = models.DateField()
    voice = models.FileField()
    deathday = models.DateField()
    status = models.CharField(max_length=20)


class Pet_day(models.Model):
    # user_id = models.ForeignKey
    user_id = models.IntegerField()
    pet_page_id = models.ForeignKey(Pet_page, on_delete=CASCADE)
    emoticon_01 = models.IntegerField()
    emoticon_02 = models.IntegerField()
    emoticon_03 = models.IntegerField()
    emoticon_04 = models.IntegerField()
    emoticon_05 = models.IntegerField()


