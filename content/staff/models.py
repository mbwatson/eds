from django.db import models
from django.template.defaultfilters import slugify

class StaffMember(models.Model):
    first_name = models.CharField(max_length=63, blank=False)
    last_name = models.CharField(max_length=63, blank=False)
    job_title = models.CharField(max_length=127, blank=False)
    slug = models.SlugField(max_length=255, editable=False, unique=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='staff_pics', blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    def display_name(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.first_name} {self.last_name}')
        super(StaffMember, self).save(*args, **kwargs)

    class Meta:
        ordering = ('last_name', 'first_name')
