from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path(r'vehicles/', views.vehicles, name='join'),
]