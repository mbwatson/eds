from django.contrib import admin
from django.urls import path
from . import views

app_name = 'staff'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:staff_id>', views.detail, name='detail'),
]
