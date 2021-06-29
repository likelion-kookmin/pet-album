from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm  #authen....로그인 해주는 폼 , UserCreationForm-회원가입 해주는 폼
from django.contrib.auth import authenticate, login, logout #contripb.auth는 회원가입 로그인하면서 여기까지는 무조건 들어간다 
from .forms import RegisterForm
# Create your views here.


def login_view(request): #로그인 창을 띄우는 함수
    if request.method == "POST":
        form = AuthenticationForm(request=request,data = request.POST)
        if form.is_valid(): #form에 대한 유효성 검사
            username = form.cleaned_data.get("username") #통과하면 username 이라는 변수를 만들어주고 username이라는 cleaned_data(유효성 검사를 통과된 클린한 데이터를 말함) 받아 username이라는걸 가져와서 변수에 저장해 
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)#user라는 객체를 만들것임, 이건 인증을 받는 객체임  authenticate(매개변수)
            if user is not None:  #user가 존재할때
                login(request, user)
        return redirect("sun")
        
    else:
        form = AuthenticationForm()
        return render(request, 'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect("home")

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