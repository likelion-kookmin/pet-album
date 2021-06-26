from django.urls import path, include
from django.urls.conf import include
from .views import *

urlpatterns = [
    path('pet_sun/',pet_sun, name='pet_sun'),
    path('pet_moon/',pet_moon, name='pet_moon'),
 ]