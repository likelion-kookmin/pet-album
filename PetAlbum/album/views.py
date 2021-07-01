from account.models import CustomUser
from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
# from .forms import AlbumForm
# from pet.models import *
# Create your views here.

# specific user albums
def album_pet(request, pet_id, user_id,pet_page_id):
  user = get_object_or_404(CustomUser, pk=user_id)
  pet = get_object_or_404(Pet, pk=pet_id)
  pet_page = get_object_or_404(Pet_page, pk=pet_page_id)
  albums = Album.objects.filter(pet_id=pet_id)
  return render(request, 'album.html', {'albums':albums, 'pet':pet, 'user':user, 'pet_page':pet_page})

def album_add(request, pet_id):
  pet = get_object_or_404(Pet, pk=pet_id)
  user = pet.user_id
  pets = Pet.objects.filter(user_id=user)
  albums = Album.objects.filter(pet_id=pet_id)
  order = request.GET.get('order', 'newest')
  if order == 'oldest':
    albums = albums.order_by('image_datetime')
  else:
    albums = albums.order_by('-image_datetime')
  # form = AlbumForm()
  return render(request, 'album_add.html', {'albums':albums, 'pets': pets})

def album_create(request, pet_id):
  # form = AlbumForm(request.POST, request.FILES)
  new_album = Album()
  new_album.is_public = request.POST['is_public']
  new_album.comment = request.POST['comment']
  new_album.image_datetime = request.POST['image_datetime']
  try:
    new_album.album_image = request.FILES['album_image']
  except:
    pass

  # set user_id
  new_album.user_id = request.user
  # set pet_id
  new_album.pet_id = get_object_or_404(Pet, pk=pet_id)

  new_album.save()
  # if form.is_valid():
  #   new_album = form.save(commit=False)
  #   new_album.save()
  #   return redirect('album_edit.html',new_album.id)
  # return redirect('album_edit',new_album.id)
  return redirect('album_edit', new_album.id)

def album_edit(request, pet_id, album_id):
  pet = get_object_or_404(Pet, pk=pet_id)
  user = pet.user_id
  pets = Pet.objects.filter(user_id=user)
  albums = Album.objects.filter(pet_id=pet_id)
  order = request.GET.get('order', 'newest')
  if order == 'oldest':
    albums = albums.order_by('image_datetime')
  else:
    albums = albums.order_by('-image_datetime')
  edit_album = get_object_or_404(Album, pk = album_id)
  return render(request, 'album_edit.html', {'albums':albums, 'album':edit_album, 'pets': pets})

def album_update(request, pet_id, album_id):
  update_album = get_object_or_404(Album, pk = album_id)
  update_album.is_public = request.POST['is_public']
  update_album.comment = request.POST.get('comment', None)
  update_album.image_datetime = request.POST['image_datetime']
  try:
    update_album.album_image = request.FILES['album_image']
  except:
    pass

  # set user_id
  update_album.user_id = request.user
  # set pet_id
  update_album.pet_id = get_object_or_404(Pet, pk=pet_id)

  update_album.save()
  return redirect('album_edit', album_id)

def album_delete(request, pet_id, album_id):
  delete_album = get_object_or_404(Album, pk = album_id)
  delete_album.delete()
  return redirect('album_add', pet_id)