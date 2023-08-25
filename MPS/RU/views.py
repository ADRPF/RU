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
            return render(request, 'home/index.html', context)
        else:
            print("Não existe esse usuário ou não está ativo")
    return render(request, 'home/pagina_login.html')

def fazer_logout(request):
    logout(request)
    return redirect('logar')


def cadastrar_aluno(request):
    if request.method == "GET":
        print('GET')
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
            print("Usuário cadastrado")
            return redirect('logar')
        else:
            print("Usuário já cadastrado")
    return render(request, 'home/pagina_cadastro.html')


#Funções do Admin
def registrarPrato(request):
    if request.method == 'POST':
        prato_nome = request.POST.get('prato_nome')
        prato_valor = request.POST.get('prato_valor')
        prato_desc = request.POST.get('prato_desc')
        prato = Prato(nome=prato_nome, valor=prato_valor, desc=prato_desc)
        prato.save()
        return
    else:
        return render(request, 'admin/cardapio/registrar_prato.html')


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

def registrarFeedback(request):
    if request.method == 'POST':
        #TODO: Salvar o feedback quando o model estiver pronto
        return
    else:
        return render(request, "corpoAcad/feedback/pagina_feedback.html")

def index(request):
    return render(request, 'home/index.html')
def ver_feedback(request):
    return render(request, 'corpoAcad/feedback/pagina_feedback.html')
