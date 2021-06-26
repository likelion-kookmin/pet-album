from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Notice

# Create your views here.


def home(request):
    blogs = Notice.objects.all()
    return render(request, 'main.html', {'blogs':blogs})

