from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from pet.models import *

# pet page (유저 연결 전, 연결 후 삭제하기)
def all(request): 
    pets = Pet.objects.all()
    return render(request, 'pet.html', {'pets': pets})

# pet page
def pet(request, pet_page_id): 
    pet_page = get_object_or_404(Pet_page, pk=pet_page_id) #펫페이지 정보를 받고 펫페이지 아이디를 받아서 페이지 객체를 불러와 #초록 펫페이지 모델임
    pets = Pet.objects.filter(pet_page_id = pet_page)
    return render(request, 'pet.html', {'pets': pets})

# pet create 아직도 이해를...
def add(request):
    if request.method == 'GET':
        return render(request, 'pet_add.html')
    else: # post method
        pet = Pet()
        # views.py에서 지정해주어야 하는 속성들
        pet.user_id = request.user
        pet.pet_page_id = get_object_or_404(Pet_page, user_id=request.user)
        # pet_add.html에서 받아온 값들 
        pet.image = request.FILES['pet_image']
        pet.name = request.POST['name']
        pet.birthday = request.POST['birthday']
        pet.voice = request.FILES['voice']
        pet.deathday = request.POST['deathday']
        pet.status = request.POST['status']
        pet.save()
        return redirect('pet', pet_page_id)

# pet update
def edit(request, pet_id):
    if request.method == 'GET':
        return render(request, 'pet_edit.html', {'pet': pet})
    else: # post method
        pet = Pet()
        # views.py에서 지정해주어야 하는 속성들
        pet.user_id = request.user
        pet.pet_page_id = get_object_or_404(Pet_page, user_id=request.user)
        # pet_add.html에서 받아온 값들 
        pet.image = request.FILES['pet_image']
        pet.name = request.POST['name']
        pet.birthday = request.POST['birthday']
        pet.voice = request.FILES['voice']
        pet.deathday = request.POST['deathday']
        pet.status = request.POST['status']
        pet.save()
        return redirect('pet', pet_page_id)

# pet delete
def delete(request, pet_id):
    to_be_deleted = get_object_or_404(Pet, pk=pet_id)
    pet_page_id = to_be_deleted.pet_page_id
    to_be_deleted.delete()
    return redirect('pet', pet_page_id)

#join result
#def join(request, user_id):
    

def sun(request):
    return

def moon(request):
    return 