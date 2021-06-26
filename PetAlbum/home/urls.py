from django.urls import path, include
from django.urls.conf import include
from .views import *

urlpatterns = [
    path('home_sun/',sun_views, name='sun'),
    path('home_moon/',moon_views, name='moon'),
 ]