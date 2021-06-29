from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
# Create your views here.

def album(request):
  albums = Album.objects.all()
  return render(request, 'album.html', {'albums':albums})

def album_add(request):
  albums = Album.objects.all()
  return render(request, 'album_add.html', {'albums':albums})

def album_edit(request, id):
  albums = Album.objects.all()
  edit_album = get_object_or_404(Album, pk = id)
  return render(request, 'album_edit.html', {'albums':albums, 'album':edit_album})

def album_update(request, id):
  update_album = get_object_or_404(Album, pk = id)
  update_album.comment = request.POST['comment']
  update_album.is_public = request.POST['is_public']
  update_album.save()
  return redirect('album_add')