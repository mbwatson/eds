from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from . import views
# Imports for handling static files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('staff/', include('content.staff.urls')),
    path('projects/', include('content.projects.urls')),
    path('publications/', include('content.publications.urls')),
    path('datasets/', include('content.datasets.urls')),
    path('blog/', include('blog.urls')),
    path(r'^tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
