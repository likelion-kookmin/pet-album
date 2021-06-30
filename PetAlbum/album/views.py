from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .forms import AlbumForm
# Create your views here.

def album(request):
  albums = Album.objects.all()
  return render(request, 'album.html', {'albums':albums})

def album_add(request):
  albums = Album.objects.all()
  order = request.GET.get('order', 'newest')
  if order == 'oldest':
    albums = albums.order_by('image_datetime')
  else:
    albums = albums.order_by('-image_datetime')
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
  # return redirect('album_edit',new_album.id)
  return redirect('album_edit', new_album.id)

def album_edit(request, album_id):
  albums = Album.objects.all()
  order = request.GET.get('order', 'newest')
  if order == 'oldest':
    albums = albums.order_by('image_datetime')
  else:
    albums = albums.order_by('-image_datetime')
  edit_album = get_object_or_404(Album, pk = album_id)
  return render(request, 'album_edit.html', {'albums':albums, 'album':edit_album})

def album_update(request, album_id):
  update_album = get_object_or_404(Album, pk = album_id)
  update_album.comment = request.POST.get('comment', None)
  update_album.image_datetime = request.POST['image_datetime']
  try:
    update_album.album_image = request.FILES['album_image']
  except:
    pass
  update_album.save()
  return redirect('album_edit', album_id)

def album_delete(request, album_id):
  delete_album = get_object_or_404(Album, pk = album_id)
  delete_album.delete()
  return redirect('album_add')