from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import lista, produtos, criarlista, criarproduto
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate


def index(request):
    return render(request, 'index.html')

def semlogin():
    return HttpResponse('Usuario sem login')

def cadastrar(request):
    if request.method == "GET":
        return render (request, 'cadastrar.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user1 = User.objects.filter(username=username).first()
        
        if user1:
            return HttpResponse("Esse user já existe")
        
        user1 = User.objects.create_user(username=username, password=senha)
        user1.save()
        return HttpResponse("Usuario cadastrado!")

def login(request):
    if request.method == "GET":
        return render (request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user1 = authenticate(username=username, password=senha)
        
        if user1:
            auth_login(request, user1)
            return HttpResponseRedirect("../visualizar")
        else:
            return HttpResponse("Email ou senha inválidos, tente novamente")


def visualizar(request):
    if request.user.is_authenticated:
        all = 0
        for tudo in produtos.objects.all():
            all = all + tudo.precoproduto
        return render(request, 'visualizar.html', {
            "lista1": lista.objects.all(), "produto1": produtos.objects.all(), "valor":all
        })
    semlogin()


def addlista(request):
    if request.user.is_authenticated:
        lista1 = criarlista(request.POST or None)

        if lista1.is_valid():
            lista1.save()
            
        return render(request, 'addlista.html', {'lista1': lista1})
    
    semlogin()


def addproduto(request):
    if request.user.is_authenticated:
        produto1 = criarproduto(request.POST or None)
        
        if produto1.is_valid():
            produto1.save()

        return render(request, 'addproduto.html', {'produto1' : produto1})
    
    semlogin()



def editarlista(request, id):
    produto = produtos.objects.get(id=id)
    if request.user.is_authenticated:
        produto1 = criarproduto(request.POST or None, instance=produto)
        
        if produto1.is_valid():
            produto1.save()
            return HttpResponseRedirect("../../visualizar")

        return render(request, 'atualizar.html', {"produtos":produto, 'produto1' : produto1})


def apagarlista(request, id):
    lista1 = lista.objects.get(id=id)
    lista1.delete()
    return HttpResponseRedirect("../../visualizar")

    

def apagarproduto(request, id):
    produto = produtos.objects.get(id=id)
    produto.delete()
    return HttpResponseRedirect("../../visualizar")
