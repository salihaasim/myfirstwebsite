from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('works/', views.works),
    path('pythondevloper/', views.pythondevloper),
    path('frontendwebdevlopment/', views.frontendwebdevlopment),
    path('backenddevloper/', views.backend),
]







