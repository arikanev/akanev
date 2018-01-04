from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page_id>/bio/', views.bio, name='bio'),
    path('<int:page_id>/software/', views.software, name='software'),
    path('<int:page_id>/publications/',
         views.publications, name='publications'),
    path('<int:page_id>/career/', views.career, name='career'),
    path('<int:page_id>/education/', views.education, name='education'),
]
