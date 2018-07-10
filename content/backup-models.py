from django.db import models

class StaffMember(models.Model):
    first_name = models.CharField(max_length=63, blank=False)
    last_name = models.CharField(max_length=63, blank=False)
    job_title = models.CharField(max_length=127, blank=False)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    def display_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ('last_name', 'first_name')

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

class Project(models.Model):
    title = models.CharField(max_length=127)
    summary = models.TextField()
    details = models.TextField()
    website = models.CharField(max_length=255, blank=True)
    staff = models.ManyToManyField(StaffMember, blank=True)
    publications = models.ManyToManyField(Publication, blank=True)

    def __str__(self):
        return self.title

class DataSet(models.Model):
    title = models.CharField(max_length=127, blank=False)
    description = models.TextField()
    link =  models.CharField(max_length=127, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
