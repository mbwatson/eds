from django.contrib import admin
from django.urls import path
from . import views

app_name = 'publications'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:publication_id>', views.detail, name='detail'),
]
