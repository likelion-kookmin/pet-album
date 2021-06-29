from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.urls.conf import include
import mypage.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mypage/', include(mypage.urls)),
    path('account/',include('account.urls')), #path연결
    path('',include('main.urls')),
    path('home/',include('home.urls')),
    path('my_pet/',include('my_pet.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)