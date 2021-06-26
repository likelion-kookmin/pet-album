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
