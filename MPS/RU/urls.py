from django.urls import path
from .views import *

urlpatterns = [
    path('inicio/', index, name='inicio'),
    path('login/', logar, name='logar'),
    path('logout/', fazer_logout, name='logout'),
    path('cadastro/', solicitarCadCA, name='cadastro'),
    path('cardapio/', consultarCardapio, name='cardapio'),
    path('cardapio/registrar_pedido/', registrarPedido, name='registrar pedido'),
    path('pedido/', visualizar_pedidos),
    path('pedido/registrar_feedback/', registrarFeedback),
    path('feedback/', ver_feedback),
    path('feedback/ver_resposta', ver_resp_feedback)
]
