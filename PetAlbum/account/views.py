from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm  #authen....로그인 해주는 폼 , UserCreationForm-회원가입 해주는 폼
from django.contrib.auth import authenticate, login, logout #contripb.auth는 회원가입 로그인하면서 여기까지는 무조건 들어간다 
from .forms import RegisterForm
# Create your views here.
from django.shortcuts import render, redirect
from .models import CustomUser
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password


def login_view(request): #로그인 창을 띄우는 함수
    if request.method == "POST":
        form = AuthenticationForm(request=request,data = request.POST)
        if form.is_valid(): #form에 대한 유효성 검사
            username = form.cleaned_data.get("username") #통과하면 username 이라는 변수를 만들어주고 username이라는 cleaned_data(유효성 검사를 통과된 클린한 데이터를 말함) 받아 username이라는걸 가져와서 변수에 저장해 
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)#user라는 객체를 만들것임, 이건 인증을 받는 객체임  authenticate(매개변수)
            if user is not None:  #user가 존재할때
                login(request, user)
            return redirect("main")
        return redirect("login")
        
    else:
        form = AuthenticationForm()
        return render(request, 'login.html',{'form':form})


# def login_view(request):
#     response_data = {}

#     if request.method == "GET" :
#         return render(request, 'login.html')

#     elif request.method == "POST":
#         login_username = request.POST.get('username', None)
#         login_password = request.POST.get('password', None)

#         if not (login_username and login_password):
#             response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
#         else : 
#             customuser = CustomUser.objects.get(username=login_username) 
#             #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
#             if check_password(login_password, customuser.password):
#                 request.session['user'] = customuser.id 
#                 #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
#                 #세션 user라는 key에 방금 로그인한 id를 저장한것.
#                 return redirect('/')
#             else:
#                 response_data['error'] = "비밀번호를 틀렸습니다."

#     return render(request, 'login.html',response_data)



# def logout_view(request):
#     logout(request)
#     return redirect("home")
# def home(request):
#     user_id = request.session.get('user')
#     if user_id :
#         customUser_info = CustomUser.objects.get(pk=user_id)  #pk : primary key
#         return HttpResponse(customUser_info.nickname)   # 로그인을 했다면, username 출력

#     return HttpResponse('로그인을 해주세요.') #session에 user가 없다면, (로그인을 안했다면)
    
    
def logout_view(request):
    request.session.pop('user')
    return redirect('home.html')


def register_view(request):
    if request.method == "POST":
        form =RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('home')
        
    else:
        form = RegisterForm()
        return render(request,'join.html',{'form':form})
