from django.shortcuts import render
from .models import *

# Create your views here.


def logar(request):
    return

def cadastrar(request):
    return

def cardapio(request):
    if request.method == 'POST':
        prato = Cardapio.objects.filter(tipoRefeicao=request.POST.get('refeicao'))
        return render(request, 'Cardapio/cardapio_carregado.html')
    return render(request, 'Cardapio/cardapio.html')

def index(request):
    return