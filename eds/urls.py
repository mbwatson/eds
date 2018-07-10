from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('staff/', include('content.staff.urls')),
    path('projects/', include('content.projects.urls')),
    path('publications/', include('content.publications.urls')),
    path('datasets/', include('content.datasets.urls')),
]
