from django import forms
from django.forms import ModelForm
from .models import Categoria, Item

class FormCategoria(ModelForm):
    class Meta:
        model = Categoria
        fields = ['id','nome']
        db_table = 'categoria'

class FormItem(ModelForm):
    class Meta:
        model = Item
        fields = ['id','descricao','categoria']
        db_table = 'item'