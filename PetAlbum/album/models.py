from django.db import models

# Create your models here.
class Album(models.Model):
    user_id = models.ForeignKey
    pet_id = models.ForeignKey
    album_image = models.ImageField(upload_to ="media/", null=True, blank=True)
    comment = models.TextField(blank=True)
    image_datetime = models.DateField()
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return "[{}] {} : {}".format(self.user_id, self.pet_id, self.comment)