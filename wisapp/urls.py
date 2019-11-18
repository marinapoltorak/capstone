from django.contrib import admin
from django.urls import path
from . import views

app_name = 'wisapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_a_scientist/', views.get_a_scientist, name='get_a_scientist'),
    path('save_a_scientist_ajax/', views.save_a_scientist_ajax, name='save_a_scientist_ajax'),
    path('signup/', views.signup, name='signup'),

]
