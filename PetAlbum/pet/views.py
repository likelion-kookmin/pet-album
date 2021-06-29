from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from models import *

# pet page
def pet(request, pet_page_id): 
    pet_page = get_object_or_404(Pet_page, pk=pet_page_id) #펫페이지 정보를 받고 펫페이지 아이디를 받아서 페이지 객체를 불러와 #초록 펫페이지 모델임
    pets = Pet.objects.filter(pet_page_id = pet_page)
    return render(request, 'pet.html', {'pets': pets})

# pet create 아직도 이해를...
def add(request):
    if request.method == 'GET':
        return render(request, 'pet_add.html')
    else:
        pet_page_id = Pet. #some code
        return redirect('pet', pet_page_id)

# pet update
def edit(request, pet_id):
    if request.method == 'GET':
        return render(request, 'pet_edit.html', {'pet': pet})
    else:
        pet_page_id= Pet. # some code
        return redirect('pet', pet_page_id)

# pet delete
def delete(request, pet_id):
    to_be_deleted = get_object_or_404(Pet, pk=pet_id)
    pet_page_id = to_be_deleted.pet_page_id
    to_be_deleted.delete()
    return redirect('pet', pet_page_id)

#join result
def join(request)