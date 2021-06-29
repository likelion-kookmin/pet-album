from django.urls import path
from . import views

app_name = 'album'

urlpatterns = [
  path('', views.album, name = "album"),
  path('add/', views.album_add, name = "album_add"),
  path('create/', views.album_create, name='album_create'),
  path('edit/<str:id>', views.album_edit, name = 'album_edit'),
  path('update/<str:id>', views.album_update, name = 'album_update'),
  path('delete/<str:id>', views.album_delete, name = 'album_delete'),
]