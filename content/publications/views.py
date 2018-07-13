from django.shortcuts import get_object_or_404, render
import requests
from django.http import HttpResponse
import json

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

# zoterou zoser key for api calls 5029621

def zotero(request):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/11')
    # response = requests.get('https://api.zotero.org/users/5029621/collections?v=3')
    items = response.json()
    return HttpResponse(json.dumps(items))

