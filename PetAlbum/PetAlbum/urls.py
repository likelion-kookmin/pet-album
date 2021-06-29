from django.contrib import admin
from django.urls import path, include
import mypage.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mypage/', include(mypage.urls)),
]