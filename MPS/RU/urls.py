from django.urls import path
from .views import *

urlpatterns = [
    path('cardapio/', consultarCardapio),
    path('registrar_cardapio/', registrarCardapio),
    path('registrar_prato/', registrarPrato),
    path('registrar_feedback/', registrarFeedback),
    path('inicio/', index),
    path('login/', logar),
    path('cadastro/', cadastrar),
]