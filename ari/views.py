from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import User

# Create your views here.


def index(request):
    user = get_list_or_404(User)
    return render(request, 'ari/index.html')


def bio(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'ari/bio.html', {'user': user})


def projects(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'ari/projects.html', {'user': user})


def publications(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'ari/publications.html', {'user': user})


def experience(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'ari/experience.html', {'user': user})


def education(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'ari/education.html', {'user': user})


def support(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'ari/support.html', {'user': user})
