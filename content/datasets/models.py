from django.db import models

class DataSet(models.Model):
    title = models.CharField(max_length=127, blank=False)
    description = models.TextField()
    link =  models.CharField(max_length=127, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
