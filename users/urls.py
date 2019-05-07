"""Defines URL patterns for users."""

from django.urls import path
from django.contrib.auth import login

from . import views

app_name = 'users'
urlpatterns = [
    # Login Page
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),
    #Logout Page
    path('logout/', views.logout_view, name='logout'),
    #Registration Page
    path('register/', views.register, name='register'),
]