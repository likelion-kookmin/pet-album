from django.urls import path
from . import views

app_name = 'album'

urlpatterns = [
  path('', views.album, name = "album"),
  path('add/', views.album_add, name = "album_add"),
  path('edit/<str:id>', views.album_edit, name = 'album_edit'),
  path('update/<str:id>', views.album_update, name = 'album_update'),
]

