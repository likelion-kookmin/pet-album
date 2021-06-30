from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Notice
from .models import Cs
from .models import Cs_comment
from django.views.generic import ListView
from django.core.paginator import Paginator

# Create your views here.

def mypage(request):
    mypages = Notice.objects.all()
    objs = Cs.objects.all()
    comments = Cs_comment.objects.all()
    return render(request, 'mypage.html', {'mypages':mypages, 'objs':objs, 'comments':comments})

def detail(request, mypage_id):
    mypage_detail = get_object_or_404(Notice, pk=mypage_id)
    return render(request, 'detail.html', {'mypage': mypage_detail})

def cs(request, obj_id):
    obj_detail = get_object_or_404(Cs, pk=obj_id)
    # find comment using obj
    comment_detail = get_object_or_404(Cs_comment, cs_id=obj_id)
    return render(request, 'cs_detail.html', {'obj':obj_detail, 'comment': comment_detail})

def cs_comment(request, comment_id):
    comment_detail = get_object_or_404(Cs_comment, pk=comment_id)
    return render(request, 'cs_detail.html', {'comment':comment_detail})

def create(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    else:
        obj = Cs()
        # save visible model data
        obj.title = request.POST['title']
        obj.contents = request.POST.get('contents', None)
        obj.cs_image = request.FILES.get('cs_image', None)
        # save invisible model data
        obj.user_id = request.user
        obj.created_date = timezone.datetime.now()
        obj.updated_date = timezone.datetime.now()
        obj.state_check = "ing"
        obj.save()
        return redirect('cs', obj.id)
