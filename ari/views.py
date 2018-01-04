from django.shortcuts import get_object_or_404, get_list_or_404, render

from .models import Page

# Create your views here.


def index(request):
    # list(Page.objects.all())
    page_list = get_list_or_404(Page.objects.all())
    return render(request, 'ari/index.html', {'page_list': page_list})


def bio(request, page_id):
    bio_page = get_object_or_404(Page, pk=page_id)
    return render(request, 'ari/bio.html', {'bio_page': bio_page})


def software(request, page_id):
    software_page = get_object_or_404(Page, pk=page_id)
    return render(request, 'ari/software.html', {'software_page': software_page})


def publications(request, page_id):
    publications_page = get_object_or_404(Page, pk=page_id)
    return render(request, 'ari/publications.html', {'publication_page': publication_page})


def career(request, page_id):
    career_page = get_object_or_404(Page, pk=page_id)
    return render(request, 'ari/career.html', {'career_page': career_page})


def education(request, page_id):
    education_page = get_object_or_404(Page, pk=page_id)
    return render(request, 'ari/education.html', {'education_page': education_page})
