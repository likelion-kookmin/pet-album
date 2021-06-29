from django.shortcuts import render

# Create your views here.
def main_views(request):
    return render(request,'main.html')

def about_us_views(request):
    return render(request,'about_us.html')