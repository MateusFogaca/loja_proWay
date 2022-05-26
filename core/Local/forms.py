from django import forms
from django.forms import ModelForm
from .models import Estado, Cidade

class FormEstado(ModelForm):
    class Meta:
        model = Estado
        fields = ['id','sigla','nome']
        db_table = 'estado'

class FormCidade(ModelForm):
    class Meta:
        model = Cidade
        fields = ['id','nome','estado']
        db_table = 'cidade'