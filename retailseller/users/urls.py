from os import name
from django.contrib import admin
from django.urls import path
from . import views 


app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name = "signup"),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('profile/', views.user_profile, name='profile'), 
]                                                                       