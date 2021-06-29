from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .forms import AlbumForm
# Create your views here.

def album(request):
  albums = Album.objects.all()
  return render(request, 'album.html', {'albums':albums})

def album_add(request):
  albums = Album.objects.all()
  form = AlbumForm()
  return render(request, 'album_add.html', {'albums':albums, 'form':form})

def album_create(request):
  # form = AlbumForm(request.POST, request.FILES)
  new_album = Album()
  new_album.comment = request.POST['comment']
  new_album.image_datetime = request.POST['image_datetime']
  try:
    new_album.album_image = request.FILES['album_image']
  except:
    pass
  new_album.save()
  # if form.is_valid():
  #   new_album = form.save(commit=False)
  #   new_album.save()
  #   return redirect('album_edit.html',new_album.id)
  return redirect('album_add')

def album_edit(request, id):
  albums = Album.objects.all()
  edit_album = get_object_or_404(Album, pk = id)
  return render(request, 'album_edit.html', {'albums':albums, 'album':edit_album})

def album_update(request, id):
  update_album = get_object_or_404(Album, pk = id)
  update_album.comment = request.POST['comment']
  update_album.save()
  return redirect('album_add')


def album_delete(request, id):
  delete_album = get_object_or_404(Album, pk = id)
  delete_album.delete()
  return redirect('album_add')