from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import pet.urls

urlpatterns = [
    path('',include('main.urls')),
    path('admin/', admin.site.urls),
    path('pet/', include(pet.urls)),
    path('album/', include('album.urls')),
    path('mypage/', include('mypage.urls')),
    path('account/',include('account.urls')), #path연결
    path('home/',include('home.urls')),
    path('my_pet/',include('my_pet.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
