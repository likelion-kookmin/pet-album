from django.db import models
from account.models import CustomUser
from pet.models import Pet

# Create your models here.
class Album(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default='')
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE, default='')
    album_image = models.ImageField(upload_to ="media/", null=True, blank=True)
    comment = models.TextField(blank=True)
    image_datetime = models.DateField()
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return "[{}] {} : {}".format(self.user_id, self.pet_id, self.comment)