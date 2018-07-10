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
    context = {
        'publication': publication,
        'staff': staff,
    }
    return render(request, 'publications/detail.html', context)