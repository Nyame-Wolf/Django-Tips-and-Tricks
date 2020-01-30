from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # authentication urls included at https://github.com/django/django/blob/stable/3.0.x/django/contrib/auth/urls.py
    path('', views.home, name="home"),
    path('register/', views.register, name='register'),
    # path('edit/', views.edit, name='edit'),
]
