from django.forms import ModelForm
from .models import TpPessoa, Cliente, Fornecedor, Usuario

class FormTpPessoa(ModelForm):
    class Meta:
        model = TpPessoa
        fields = ['id','descricao']
        db_table = 'TpPessoa'

class FormCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = ['id','nome','email','cpfcnpj','tp_pessoa','estado','cidade']
        db_table = 'cliente'

class FormFornecedor(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['id','nome','fantasia','email','cpfcnpj','tp_pessoa','estado','cidade']
        db_table = 'fornecedor'

class FormUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields = ['id','nome','sobrenome','login','senha']
        db_table = 'usuario'