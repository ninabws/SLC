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
        user = request.POST.get('user')
        senha = request.POST.get('senha')
        user1 = User.objects.filter(user=user, password=senha).first()
        
        if user1:
            return HttpResponse("Esse user já existe")
        
        user1 = User.objects.create_user(user=user1, password=senha)
        user1.save()
        return HttpResponse("Usuario cadastrado!")

def login(request):
    if request.method == "GET":
        return render (request, 'login.html')
    else:
        user = request.POST.get('user')
        senha = request.POST.get('senha')
        user1 = authenticate(user=user1, password=senha)
        
        if user:
            auth_login(request, user)
            return HttpResponseRedirect("../verlista")
        else:
            return HttpResponse("Email ou senha inválidos, tente novamente")


def verlista(request):
    if request.user.is_authenticated:
        return render(request, 'verlista.html', {
            "lista": lista.objects.all(), "produtos": produtos.objects.all
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
            return HttpResponseRedirect("../../verlista")

        return render(request, 'editar.html', {"produtos":produto, 'produto1' : produto1})


def apagarlista(request, id):
    lista = lista.objects.get(id=id)
    lista.delete()
    return HttpResponseRedirect("../../verlista")

    

def apagarproduto(request, id):
    produto = produtos.objects.get(id=id)
    produto.delete()
    return HttpResponseRedirect("../../verlista")
