from django.urls import path
import album.views as views

# app_name = 'album'

urlpatterns = [
  path('<int:pet_id>', views.album_pet, name = "album_pet"), # specific user + specific pet
  path('<int:pet_id>/add/', views.album_add, name = "album_add"),
  path('<int:pet_id>/create/', views.album_create, name='album_create'),
  path('<int:pet_id>/edit/<int:album_id>', views.album_edit, name = 'album_edit'),
  path('<int:pet_id>/update/<int:album_id>', views.album_update, name = 'album_update'),
  path('<int:pet_id>/delete/<int:album_id>', views.album_delete, name = 'album_delete'),
]