from django.shortcuts import render
from .models import Album
# Create your views here.

def album(request):
  albums = Album.objects.all()
  return render(request, 'album.html')

def album_add(request):
  return render(request, 'album_add.html')