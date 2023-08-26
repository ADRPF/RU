from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
from datetime import datetime

# Create your views here.

#Funções de Usuário
def logar(request):
    if request.method == 'POST':
        nome = request.POST.get('username')
        senha = request.POST.get('senha')
        user = authenticate(request, username=nome, password=senha)
        if user is not None:
            login(request, user)
            ca = CorpoAcad.objects.get(usuario=user)
            context = {'nome': user.username,
                       'matricula': ca.matricula}
            return redirect('inicio')
        else:
            print("Não existe esse usuário ou não está ativo")
    return render(request, 'home/pagina_login.html')

def fazer_logout(request):
    logout(request)
    return redirect('logar')


def index(request):
    if request.user.is_authenticated:
        usuario = CorpoAcad.objects.get(usuario=request.user.pk)
        context = {'nome': request.user.username,
                   'matricula': usuario.matricula}
        return render(request,'home/index.html', context)
    else:
        return redirect('logar')


def solicitarCadCA(request):
    if request.method == "GET":
        return render(request, 'home/pagina_cadastro.html')
    if request.method == "POST":
        nome = request.POST.get('nome')
        matricula = request.POST.get('matricula')
        senha = request.POST.get('senha')
        data = request.POST.get('data')
        sexo = request.POST.get('sexo')
        status = False
        if not User.objects.filter(username=nome).exists():
            user = User.objects.create_user(username=nome, password=senha, is_active=status)
            user.save()
            usuario = CorpoAcad(usuario=user, matricula=matricula, dtNascimento=data, sexo=sexo)
            usuario.save()
            return redirect('logar')
    return render(request, 'home/pagina_cadastro.html')


# Funcões do Corpo Academico
def registrarCardapio(request):
    if request.method == 'POST':
        refeicao = request.POST.get('refeicao')
        dia = request.POST.get('dia')
        prato = request.POST.get('prato')
        cardapio = Cardapio(tipoRefeicao=refeicao, diaRefeicao=dia)
        cardapio.save()
        cardapio.prato.add(prato)
        return HttpResponse('Item Cadastrado')
    else:
        pratos = Prato.objects.all()
        context = {'pratos': pratos}
        return render(request, 'admin/cardapio/registrar_cardapio.html', context)

def consultarCardapio(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            # Recarrega a página com as instâncias de prato relacionados com a refeicao e dia selecionados
            refeicao, dia = request.POST.get('refeicao'), request.POST.get('data') # faz o get nos campos refeicao e data
            cardapio = Cardapio.objects.filter(tipoRefeicao=refeicao, diaRefeicao=dia) # consulta os itens do cardapio
            pratos_queryset_list = [c.prato.all() for c in cardapio] # cria uma lista de todos os pratos do cardapio
            pratos = []
            for p in pratos_queryset_list:
                pratos.append({'id': p[0].pk, 'nome': p[0].nome, 'valor': p[0].valor, 'desc': p[0].desc}) # concatena os atributos de prato para o context
            context = {'pratos': pratos}
            return render(request, 'corpoAcad/cardapio/cardapio_carregado.html', context=context)
        else:
            # Carrega a página na primeira requisação ao servidor.
            return render(request, 'corpoAcad/cardapio/cardapio.html')
    else:
        return redirect('logar')


def registrarPedido(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pratoId = request.POST.get('pratoId')
            print(pratoId)
            formaPag = request.POST.get('formaPag')
            pedido = Pedido(formaPag=formaPag, corpoAcad=request.user)
            pedido.save()
            pedido.prato.set(pratoId)
            return redirect('inicio')
        else:
            return render(request, 'corpoAcad/cardapio/registrar_pedido.html')
    else:
        return redirect('logar')


def visualizar_pedidos(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            dia = request.POST.get('dia')
            print(dia)
            pedidos_qs = Pedido.objects.filter(corpoAcad=request.user.pk, diaCompra=dia)
            pedidos = pedidos_qs.all()
            context = {'pedidos': pedidos}
            return render(request, 'corpoAcad/pedido/visualizar_pedido.html', context)
        else:
            return render(request, 'corpoAcad/pedido/pedido.html')
    else:
        return redirect('logar')


def registrarFeedback(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            mensagem = request.POST.get('fixedTextarea')
            print(mensagem)
            pedidoId = request.POST.get('pedidoId')
            pedido = Pedido.objects.get(pk=pedidoId)
            feedback = Feedback(mensagem=mensagem, respondido=False, resposta='')
            feedback.save()
            pedido.feedback = feedback
            pedido.save()
            #TODO: Salvar o feedback quando o model estiver pronto
            return redirect('pedido')
        else:
            context = {'pedidoId': request.GET.get('pedidoId')}
            return render(request, "corpoAcad/feedback/pagina_feedback.html", context)
    else:
        return redirect('logar')


def ver_feedback(request):
    if request.user.is_authenticated:
        pedidoId = request.GET.get('pedidoId')
        pedido = Pedido.objects.get(pk=pedidoId)
        mensagem = pedido.feedback.mensagem
        resposta = pedido.feedback.resposta
        context = {'pedidoId': pedidoId,
                   'mensagem': mensagem,
                   'resposta': resposta}
        return render(request, 'corpoAcad/feedback/visualizar_resposta.html', context)
    else:
        return redirect('logar')
