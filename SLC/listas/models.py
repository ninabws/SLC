from django.db import models
from django.forms import ModelForm

# Create your models here.

class lista(models.Model):
    nomelista = models.CharField(max_length=80)   
    
    def __str__(self):
        return self.nomelista

class produtos(models.Model):
    nomeproduto = models.CharField(max_length=80, default= None)
    precoproduto = models.FloatField(default= 0)
    lista2 = models.ForeignKey(lista, on_delete=models.CASCADE, related_name="departures")
    
    def __str__(self):
        return self.nomeproduto

class criarlista(ModelForm):
    class Meta:
        model = lista
        fields = ['nomelista']

class criarproduto(ModelForm):
    class Meta:
        model = produtos
        fields = ['nomeproduto', 'precoproduto']