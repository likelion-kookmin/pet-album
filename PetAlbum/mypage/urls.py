'''from PetAlbum.mypage import views
from django.urls import path
from . import views

app_name = 'mypage'

urlpatterns = [
    path('', views.NoticeListView.as_view(), name="notice_list"),
    path('create/', views.create, name="create"),
    path('cs/<int:obj_id>', views.cs, name="cs"),
]
'''

from django.urls import path
from .views import *


urlpatterns = [
    # path('', NoticeListView.as_view(), name="notice_list"),
    path('', home, name='home'),
    path('detail/<int:mypage_id>', detail, name='detail'),
    path('cs/<int:obj_id>', cs, name="cs"),
    path('create/', create, name="create"),
]