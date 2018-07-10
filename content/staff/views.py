from django.shortcuts import get_object_or_404, render

from .models import StaffMember

def index(request):
    staff_members = StaffMember.objects.all()
    context = {
        'staff': staff_members
    }
    return render(request, 'staff/index.html', context)

def detail(request, staff_id):
    staff_member = get_object_or_404(StaffMember, id=staff_id)
    projects = staff_member.project_set.all()
    publications = staff_member.publication_set.all()
    context = {
        'staff_member': staff_member,
        'projects': projects,
        'publications': publications,
    }
    return render(request, 'staff/detail.html', context)