from django.shortcuts import get_object_or_404, render

from .models import Project

def index(request):
    projects = Project.objects.all()
    context = {
        'page_title': 'Projects',
        'projects': projects
    }
    return render(request, 'projects/index.html', context)


def detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    staff = project.staff.all()
    publications = project.publications.all()
    context = {
        'page_title': project.title,
        'project': project,
        'staff': staff,
        'publications': publications,
    }
    return render(request, 'projects/detail.html', context)