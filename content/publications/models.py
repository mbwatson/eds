from django.db import models
from content.staff.models import StaffMember

class Publication(models.Model):
    title = models.CharField(max_length=200, blank=False)
    abstract = models.TextField(blank=True)
    link = models.CharField(max_length=200, blank=True)
    citation = models.TextField(blank=True)
    staff = models.ManyToManyField(StaffMember, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
