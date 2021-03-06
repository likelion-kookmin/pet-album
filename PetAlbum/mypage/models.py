from django.db import models
from django.db.models.deletion import CASCADE
from account.models import CustomUser
from django.conf import settings
from account.models import *

# Create your models here.
class Notice(models.Model):
    #user_id = models.ForeignKey('account.CustomUser', on_delete=CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    contents = models.TextField(null=True)
    created_date = models.DateField(auto_now_add=True) #수정 안됨
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Cs(models.Model):
    #user_id = models.ForeignKey(User, on_delete=CASCADE)
    #user_id = models.ForeignKey('account.CustomUser', on_delete=CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    contents = models.TextField(null=True)
    created_date = models.DateField(auto_now_add=True) #수정 안됨
    updated_date = models.DateField(auto_now=True)
    cs_image = models.ImageField(null=True)
    state_choices = (
        ("처리중", "ing"),
        ("처리완료", "finished"),
    )
    state_check = models.CharField(max_length=50, choices=state_choices)

    # 처리중 / 처리 완료
    # finish_check = models.BooleanField()

    def __str__(self):
        return self.title #들어온 객체의 타이틀을 써줘 
    

class Cs_comment(models.Model):
    #user_id = models.ForeignKey('account.CustomUser', on_delete=CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    cs_id = models.ForeignKey('mypage.Cs', on_delete=CASCADE)
    content = models.TextField(null=True)
    created_date = models.DateField(auto_now_add=True) #수정 안됨
    updated_date = models.DateField(auto_now=True)
