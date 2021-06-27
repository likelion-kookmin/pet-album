from django.db import models

# Create your models here.
class Album(models.Model):
    user_id = models.ForeignKey
    pet_id = models.ForeignKey
    album_image = models.ImageField(upload_to ="image_upload_path", null=True, blank=True)
    comment = models.TextField(null=True)
    image_datetime = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)