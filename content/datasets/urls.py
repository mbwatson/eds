from django.contrib import admin
from django.urls import path
from . import views

app_name = 'datasets'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:dataset_id>', views.detail, name='detail'),
]
