from django.shortcuts import get_object_or_404, render

from .models import Publication

def index(request):
    publications = Publication.objects.all()
    context = {
        'page_title': 'Publications',
        'publications': publications
    }
    return render(request, 'publications/index.html', context)

def detail(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    staff = publication.staff.all()
    projects = publication.projects.all()
    context = {
        'page_title': publication.title,
        'publication': publication,
        'staff': staff,
        'projects': projects,
    }
    return render(request, 'publications/detail.html', context)