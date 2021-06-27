from PetAlbum.blog import views
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.NoticeListView.as_view(), name="notice_list"),
    path('create/', views.create, name="create"),
    path('cs/', views.cs, name="cs"),
    path('postcreate/', views.postcreate, name='postcreate'),
]
