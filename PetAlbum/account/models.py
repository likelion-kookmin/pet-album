from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.forms import AuthenticationForm,User
# Create your models here.

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=50)
    user_image = models.ImageField
    pet = models.CharField(max_length=20)


