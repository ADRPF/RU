from django.urls import path
from .views import *

urlpatterns = [
    path('cardapio/', consultarCardapio),
    path('registrar_cardapio/', registrarCardapio),
    path('registrar_prato/', registrarPrato),
    path('registrar_feedback/', registrarFeedback),
    path('inicio/', index, name='inicial'),
    path('login/', logar, name='logar'),
    path('cadastro/', cadastrar_aluno),
    path('feedback/', ver_feedback)
]
