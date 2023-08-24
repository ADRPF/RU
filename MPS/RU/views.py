from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import datetime

# Create your views here.


def logar(request):
    return

def cadastrar(request):
    return

def registrarCardapio(request):
    #função de teste que cria 5 instâncias de cardapio relacionados com o prato de Testes.
    p = Prato.objects.filter(pk=1)
    for _ in range(5):
        c = Cardapio(tipoRefeicao=CAFE_MANHA, diaRefeicao=datetime.now())
        c.save()
        c.prato.add(p[0])
    return HttpResponse('Objetos Criados')

def cardapio(request):
    if request.method == 'POST':
        # Recarrega a página com as instâncias de prato relacionados com a refeicao e dia selecionados
        refeicao, dia = request.POST.get('refeicao'), request.POST.get('data') # faz o get nos campos refeicao e data
        cardapio = Cardapio.objects.filter(tipoRefeicao=refeicao, diaRefeicao=dia) # consulta os itens do cardapio
        prato = cardapio[0].prato.all() # acessa os atributos de prato relacionado com os do cardapio
        context = {'pratos': prato}

        return render(request, 'Cardapio/cardapio_carregado.html', context=context)
    else:
        # Carrega a página na primeira requisação ao servidor.
        return render(request, 'Cardapio/cardapio.html')

def index(request):
    return