from django.urls import path
from .views import *

urlpatterns = [
    path('cardapio/', cardapio),
    path('registrar', registrarCardapio),
    path('inicio/', index),
    path('login/', logar),
    path('cadastro/', cadastrar),
]