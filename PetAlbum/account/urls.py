from django.urls import path
from django.urls.resolvers import URLPattern
from .views import * #views.py의 모든 함수를 가지고 온다는 문법임 

urlpatterns = [
    path('login/',login_view, name = "login"), #요청받을 url, 함수이름, 네임=로그인 / 여기 입력했으면 프로젝트 urls.py가서 path연결해줘야함 
    path('logout/',logout_view, name="logout"),
    path('join/',register_view, name="join"),
]
