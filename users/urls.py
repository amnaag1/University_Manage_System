from django.urls import path
from . import views

urlpatterns = [
    path('', views.users, name='home'),
    path('users/', views.users, name='users'),
]
