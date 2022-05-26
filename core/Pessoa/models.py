from django.db import models
from Local.models import Estado, Cidade

# Create your models here.
class TpPessoa(models.Model):
    descricao = models.CharField(max_length=50, unique=True, blank=False)

    class Meta:
        db_table = 'TpPessoa'
    
    def __str__(self):
        return self.descricao

class Cliente(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=100, unique=True)
    cpfcnpj = models.CharField(max_length=14, blank=False, unique=True)
    tp_pessoa = models.ForeignKey(TpPessoa,on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE)


    class Meta:
        db_table = 'Cliente'
    
    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    fantasia = models.CharField(max_length=100, blank=False, unique=True)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    cpfcnpj = models.CharField(max_length=14, blank=False, unique=True)
    tp_pessoa = models.ForeignKey(TpPessoa, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade,on_delete=models.CASCADE)

    class Meta:
        db_table = 'Fornecedor'
    
    def __str__(self):
        return self.nome

class Usuario(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    sobrenome = models.CharField(max_length=50, blank=False)
    login = models.CharField(max_length=50, blank=False, unique=True)
    senha = models.CharField(max_length=50, blank=False)

    class Meta:
        db_table = 'Usuario'
    
    def __str__(self):
        return self.nome