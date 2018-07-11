from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:post_slug>', views.detail, name='detail'),
    path('<slug:category_slug>', views.category, name='category'),
]
