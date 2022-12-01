from django.contrib import admin
from django.urls import path
from . import views
from asyncore import dispatcher_with_send

urlpatterns = [
    path('',views.palestra),
    path('cadastro',views.cadastrar),
    path('alunos', views.listar)
    

]
