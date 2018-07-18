from django.shortcuts import get_object_or_404, get_list_or_404, render
import requests
from django.http import HttpResponse
import json
from django.utils.http import urlunquote

from .models import Publication
from .models import StaffMember

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

def zotero(request):
    import pyzotero
    from pyzotero import zotero
    # Retrieve collection name from url
    collection_name = request.GET.get('collection')
    credentials = get_object_or_404(ZoteroCollection, name=urlunquote(collection_name))
    # Pull collection from Zotero
    zot = zotero.Zotero(credentials.group_id, 'group', credentials.api_key)
    items = zot.collection_items(credentials.collection_id)
    # Load subset of collection data into `publications` list
    publications = []
    itemTypes = { item['data'].get('itemType') for item in items }
    for itemType in itemTypes:
        subCollection = [ {
            'key': item['data'].get('key'),
            'title': item['data'].get('title'),
            'abstract': item['data'].get('abstractNote', None),
            'authors': makeAuthorsList(item['data'].get('creators', None)),
        } for item in items if item['data'].get('itemType') == itemType ]
        publications.append({
            itemType: subCollection
        })
    # Load and send staff slugs along for backlinking to staff pages
    staff = get_list_or_404(StaffMember)
    staffSlugs = [ staffMember.slug for staffMember in staff ]
    context = {
        'publications': publications,
        'staffSlugs': staffSlugs
    }
    return render(request, 'publications/zotero.html', context)
