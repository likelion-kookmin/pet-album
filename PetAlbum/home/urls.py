from django.urls import path, include
from django.urls.conf import include
from .views import *

urlpatterns = [
    path('sun/',sun_views, name='sun'),
    path('moon/',moon_views, name='moon'),
 ]