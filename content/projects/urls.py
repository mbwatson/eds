from django.contrib import admin
from django.urls import path
from content.projects import views

app_name = 'projects'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:project_id>', views.detail, name='detail'),
]
