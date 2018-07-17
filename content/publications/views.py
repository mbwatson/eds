from django.shortcuts import get_object_or_404, get_list_or_404, render
import requests
from django.http import HttpResponse
import json

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

# zoterou zoser key for api calls 5029621
# API Key : Tdi0yxJ5mIS3Q2F3unAVf9UH

def makeFullName(creatorObject):
    if 'firstName' in creatorObject and 'lastName' in creatorObject:
        return f"{creatorObject['firstName']} {creatorObject['lastName']}"
    return ""

def makeAuthorsList(creatorsList):
    authors = []
    if creatorsList:
        for creator in creatorsList:
            authors.append(makeFullName(creator))
        return authors
    return []

def zotero(request):
    import pyzotero
    from pyzotero import zotero
    import yaml

    with open("config.yaml", 'r') as ymlfile:
        config = yaml.load(ymlfile)
    zot = zotero.Zotero(config['zotero']['group_id'], 'group', config['zotero']['api_key'])
    items = zot.collection_items(config['zotero']['collection_id'])
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
    staff = get_list_or_404(StaffMember)
    staffSlugs = [ staffMember.slug for staffMember in staff ]
    context = {
        'publications': publications,
        'staffSlugs': staffSlugs
    }
    return render(request, 'publications/zotero.html', context)
