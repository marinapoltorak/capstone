from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'wisapp'
urlpatterns = [
    path('scientist/', views.get_scientist, name='get_scientist'),
]
