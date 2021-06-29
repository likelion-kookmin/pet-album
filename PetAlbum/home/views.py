from django.shortcuts import render

# Create your views here.
def sun_views(request):
    return render(request,'home_sun.html')

def moon_views(request):
    return render(request,'home_moon.html')

