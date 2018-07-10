from django.db import models
from content.staff.models import StaffMember
from content.publications.models import Publication

class Project(models.Model):
    title = models.CharField(max_length=127)
    summary = models.TextField()
    details = models.TextField()
    website = models.CharField(max_length=255, blank=True)
    staff = models.ManyToManyField(StaffMember, blank=True)
    publications = models.ManyToManyField(Publication, blank=True)

    def __str__(self):
        return self.title
