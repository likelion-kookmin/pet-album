from PetAlbum.blog import views
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.NoticeListView.as_view(), name="notice_list"),
]
