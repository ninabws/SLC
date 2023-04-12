from django.urls import path
from . import views

app_name = "listas"
urlpatterns = [
    path('', views.index, name='index'),
    path('auth/cadastrar', views.cadastrar, name='cadastrar'),
    path('auth/login', views.login, name='login'),
    path('verlista', views.verlista, name='verlista'),
    path('addlista', views.addlista, name='addlista'),
    path('addproduto', views.addproduto, name='addproduto'),
    path('editarlista/<int:id>/', views.editarlista, name='editarlista'),
    path('apagarlista/<int:id>/', views.apagarlista, name='apagarlista'),
    path('apagarproduto/<int:id>/', views.apagarproduto, name='apagarproduto'),
    
]
