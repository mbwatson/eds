from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=255,null=False)
    description = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['-create_date']
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Post(models.Model):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Final', 'Final'),
    )
    title = models.CharField(max_length=255,null=False)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Draft')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def published(self):
        past_publish_date = self.publish_date <= timezone.now()
        has_publish_status = self.status == 'Final'
        return past_publish_date and has_publish_status
    
