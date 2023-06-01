from django.contrib import admin
from django.urls import path, url
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    url(r'^historias/', views.historia_list, name='historiaList'),
    url(r'historia/<id>', views.single_historia, name='singleHistoria'),
    url(r'historiacreate/$', csrf_exempt(views.historia_create), name='historiacreate'),
]
