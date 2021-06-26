from django.urls import path
from .views import *

urlpatterns = [
    path('',main_views, name='main'),
    path('about_us/',about_us_views, name='about_us'),
]