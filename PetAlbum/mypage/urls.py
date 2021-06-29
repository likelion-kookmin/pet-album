from django.urls import path
from .views import *


urlpatterns = [
    # path('', NoticeListView.as_view(), name="notice_list"),
    path('', mypage, name='mypage'),
    path('detail/<int:mypage_id>', detail, name='detail'),
    path('cs/<int:obj_id>', cs, name="cs"),
    path('create/', create, name="create"),
]