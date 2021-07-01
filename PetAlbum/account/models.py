from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.forms import AuthenticationForm,User
# Create your models here.

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=50)
    user_image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    pet_choices = (
		('Y', '있음'),
        ('N', '없음'),
    )
    # pet = models.CharField(max_length=2, choices=pet_choices, blank=True)
    # like= models.ManyToManyField('Pet_day', blank=True, related_name='like_user')
 