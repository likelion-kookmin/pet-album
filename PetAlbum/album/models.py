from django.db import models

# Create your models here.
class Album(models.Model):
    user_id = models.ForeignKey
    pet_id = models.ForeignKey
    album_image = models.ImageField(upload_to ="media/", null=True, blank=True)
    comment = models.TextField(blank=True)
    image_datetime = models.DateTimeField()
    is_public = models.BooleanField(default=True)