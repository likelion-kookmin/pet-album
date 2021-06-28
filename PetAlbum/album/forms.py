from django import forms
from django.forms import fields
from .models import Album


class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album
    fields = ['album_image', 'comment', 'image_datetime', 'is_public']
