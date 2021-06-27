from django.db import models

# Create your models here.
class Notice(models.Model):
    user_id = models.ForeignKey
    title = models.CharField(max_length=100)
    contents = models.TextField(null=True)
    created_date = models.DateField(auto_now_add=True) #수정 안됨
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Cs(models.Model):
    user_id = models.ForeignKey
    title = models.CharField(max_length=100)
    contents = models.TextField(null=True)
    created_date = models.DateField(auto_now_add=True) #수정 안됨
    updated_date = models.DateField(auto_now=True)
    cs_image = models.ImageField(null=True)
    state_check = models.CharField(max_length=50)

    def __str__(self):
        return self.title #들어온 객체의 타이틀을 써줘 
    

class Cs_comment(models.Model):
    user_id = models.ForeignKey
    cs_id = models.ForeignKey
    comment = models.TextField
    created_date = models.DateField(auto_now_add=True) #수정 안됨
    updated_date = models.DateField(auto_now=True)
