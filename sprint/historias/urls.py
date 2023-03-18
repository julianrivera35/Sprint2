from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.historias_view, name='historias_view'),
    path('<int:pk>', views.historia_view, name='historia_view'),
]