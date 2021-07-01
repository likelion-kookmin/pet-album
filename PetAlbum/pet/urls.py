from django.urls import path
import pet.views as views

urlpatterns = [
    path('', views.all, name='all'), #전체 유저의 펫 페이지 열기 (테스트용) - 유저 연결 후 삭제하기!
    path('<int:pet_page_id>', views.pet, name='pet'), #pet메인페이지에서 특정 유저의 페이지를 열어요
    path('add/', views.add, name='add'),#만들고
    path('edit/<int:pet_id>', views.edit, name='edit'),#수정해요 #어떤걸 수정할지 필요하니까 url로 int 저거 주는거임
    path('delete/<int:pet_id>', views.delete, name='delete'),#지워요 #위에거와 같음

   
    path('sun', views.sun, name='sun'),
    path('moon', views.moon, name='moon'),
    #join
]
