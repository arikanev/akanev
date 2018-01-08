from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/bio/', views.bio, name='bio'),
    path('<int:user_id>/projects/', views.projects, name='projects'),
    path('<int:user_id>/publications/',
         views.publications, name='publications'),
    path('<int:user_id>/experience/', views.experience, name='experience'),
    path('<int:user_id>/education/', views.education, name='education'),
    path('<int:user_id>/support/', views.support, name='support'),
]
