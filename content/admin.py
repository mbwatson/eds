from django.contrib import admin
from content.staff.models import StaffMember
from content.projects.models import Project
from content.publications.models import Publication
from content.datasets.models import DataSet
from content.zotero.models import Collection
from django.contrib import admin

class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'slug',)
    exclude = ('slug',)

admin.site.register(StaffMember, StaffMemberAdmin)

admin.site.register(Project)

admin.site.register(Publication)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'group_id', 'collection_id',)

admin.site.register(Collection, CollectionAdmin)

admin.site.register(DataSet)
