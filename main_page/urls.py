from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('dashboard/', views.dashboard, name='main-dashboard'),
]