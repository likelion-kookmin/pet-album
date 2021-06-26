from django.shortcuts import render

# Create your views here.
def pet_sun(request):
    return render(request,'pet_sun.html')

def pet_moon(request):
    return render(request,'pet_moon.html')