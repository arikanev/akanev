from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bio/', views.bio, name='bio'),
    path('projects/', views.projects, name='projects'),
    path('publications/',
         views.publications, name='publications'),
    path('experience/', views.experience, name='experience'),
    path('education/', views.education, name='education'),
]
