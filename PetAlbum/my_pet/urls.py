from django.urls import path, include
from django.urls.conf import include
from .views import *

urlpatterns = [
    path('sun/',pet_sun, name='pet_sun'),
    path('moon/',pet_moon, name='pet_moon'),
 ]