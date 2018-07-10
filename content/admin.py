from django.contrib import admin
from content.staff.models import StaffMember
from content.projects.models import Project
from content.publications.models import Publication
from content.datasets.models import DataSet

admin.site.register(StaffMember)
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(DataSet)
