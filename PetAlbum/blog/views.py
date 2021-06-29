from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Notice
from .models import Cs
from django.views.generic import ListView
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    blogs = Notice.objects.all()
    objs = Cs.objects.all()
    return render(request, 'main.html', {'blogs':blogs, 'objs':objs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Notice, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})

def cs(request, obj_id):
    obj_detail = get_object_or_404(Cs, pk=obj_id)
    return render(request, 'cs_detail.html', {'obj':obj_detail})

def create(request):
    return render(request, 'create.html')

def postcreate(request):
    obj = Cs()
    obj.title = request.GET.get('title')
    obj.contents = request.GET.get('contents')
    obj.updated_date = timezone.datetime.now()
    obj.save()
    return redirect('cs', obj.id)