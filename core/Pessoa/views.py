
from django.shortcuts import render, redirect
from .forms import FormCliente, FormFornecedor, FormTpPessoa, FormUsuario
from .models import Cliente, Fornecedor, TpPessoa, Usuario
from Local.models import Estado, Cidade
from ViewsProject.views import efetua_paginacao

# Create your views here.
def lista_tp_pessoas(request):
    procura = request.GET.get('procura')

    if procura:
        tipoPessoa = TpPessoa.objects.filter(descricao__icontains=procura)
    else:
        tipoPessoa = TpPessoa.objects.all()
    total = tipoPessoa.count

    dados = { 
        'tipos' : tipoPessoa,
        'total' : total, 
        'procura': procura,
        'porPagina':efetua_paginacao(request, tipoPessoa) 
        }
    return render(request,'lista_tp_pessoa.html',dados)



def cadastra_tp_pessoa(request):
    if request.method == 'POST':
        form = FormTpPessoa(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_tp_pessoas)
    return render(request,'cadastra_tp_pessoa.html')

def altera_tp_pessoa(request,id):
    tipo = TpPessoa.objects.get(id=id)
    if request.method == 'POST':
        form = FormTpPessoa(request.POST,instance=tipo)
        if form.is_valid():
            form.save()
            return redirect(lista_tp_pessoas)
    return render(request,'altera_tp_pessoa.html',{ 'tipo' : tipo })

def exclui_tp_pessoa(request, id):
    tipo = TpPessoa.objects.get(id=id)

    if request.method == 'POST':
        tipo.delete()
        return redirect(lista_tp_pessoas)

    return render(request,'exclui_tp_pessoa.html', {'tipo': tipo})
#CLIENTES#
def lista_clientes(request):
    procura = request.GET.get('procura')

    if procura:
        cliente = Cliente.objects.filter(nome__icontains=procura)|Cliente.objects.filter(email__icontains=procura)
    else:
        cliente = Cliente.objects.all()

    total = cliente.count

    dados = { 
        'cliente'  : cliente, 
        'total'    : total, 
        'procura'  : procura,
        'porPagina': efetua_paginacao(request, cliente) 
        }
    return render(request,'lista_clientes.html',dados)

def cadastra_cliente(request):
    tp_pessoa = TpPessoa.objects.all()
    estados = Estado.objects.all()
    cidades = Cidade.objects.all()
    if request.method == 'POST':
        form = FormCliente(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_clientes)
    return render(request,'cadastra_cliente.html',{'tipo' : tp_pessoa, 'estados': estados, 'cidades': cidades})

def altera_cliente(request,id):
    cliente = Cliente.objects.get(id=id)
    tipo = TpPessoa.objects.all()
    estados = Estado.objects.all()
    cidades = Cidade.objects.all()
    tipoCliente = TpPessoa.objects.get(id=cliente.tp_pessoa_id)
    estadoCliente = Estado.objects.get(id=cliente.estado_id)
    cidadeCliente = Cidade.objects.get(id=cliente.cidade_id)
    dados = { 
                'cliente' : cliente, 
                'tipos' : tipo, 
                'tipoPessoa' : tipoCliente,
                'estados' : estados,
                'cidadesS' : cidades,
                'estadoCliente':estadoCliente.id,
                'cidadeCliente':cidadeCliente.id
            }
    if request.method == 'POST':
        form = FormCliente(request.POST,instance=cliente)
        if form.is_valid():
            form.save()
            return redirect(lista_clientes)
    return render(request,'altera_cliente.html',dados)

def exclui_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    tipo = TpPessoa.objects.get(id=cliente.tp_pessoa_id)
    estados = Estado.objects.get(id=cliente.estado_id)
    cidades = Cidade.objects.get(id=cliente.cidade_id)

    if request.method == 'POST':
        cliente.delete()
        return redirect(lista_clientes)

    dados = {
        'cliente': cliente,
        'tipo':tipo,
        'estados':estados,
        'cidades':cidades
        }
    return render(request,'exclui_cliente.html',dados)
#FORNECEDORES#
def lista_fornecedores(request):
    procura = request.GET.get('procura')

    if procura:
        fornecedores = Fornecedor.objects.filter(fantasia__icontains=procura)
    else:
        fornecedores = Fornecedor.objects.all()
    total = fornecedores.count

    dados = { 
        'fornecedores' : fornecedores, 
        'total' : total, 
        'procura': procura,
        'porPagina': efetua_paginacao(request, fornecedores) 
        }
    return render(request,'lista_fornecedores.html',dados)

def cadastra_fornecedor(request):
    tipo = TpPessoa.objects.all()
    estados = Estado.objects.all()
    cidades = Cidade.objects.all()
    if request.method == 'POST':
        form = FormFornecedor(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_fornecedores)

    return render(request,'cadastra_fornecedor.html',{'tipos':tipo,'estados': estados,'cidades': cidades})

def altera_fornecedor(request, id):
    fornecedor = Fornecedor.objects.get(id=id)
    form = FormFornecedor(request.POST, instance=fornecedor)
    tppessoa = TpPessoa.objects.all()
    estados = Estado.objects.get(id=fornecedor.estado_id)
    cidades = Cidade.objects.get(id=fornecedor.cidade_id)
    tipoFornecedor = TpPessoa.objects.get(id=fornecedor.tp_pessoa_id)
    estadoForn = Estado.objects.get(id=fornecedor.estado_id)
    cidadeForn = Cidade.objects.get(id=fornecedor.cidade_id)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_fornecedores)
    
    dados = {
        'fornecedor' : fornecedor,
        'tipoPessoa' : tppessoa,
        'tipoFornecedor' : tipoFornecedor,
        'estados' : estados,
        'cidades' : cidades,
        'estadoForn':estadoForn.id,
        'cidadeForn':cidadeForn.id
    }

    return render(request,'altera_fornecedor.html',dados)

def exclui_fornecedor(request,id):
    fornecedor = Fornecedor.objects.get(id=id)
    tipo = TpPessoa.objects.get(id=fornecedor.tp_pessoa_id)
    estado = Estado.objects.get(id=fornecedor.estado_id)
    cidade = Cidade.objects.get(id=fornecedor.cidade_id)
    
    if request.method == 'POST':
        fornecedor.delete()
        return redirect(lista_fornecedores)

    dados = {
        'forn':fornecedor,
        'tipo':tipo, 
        'estado':estado,
        'cidade':cidade
        }
    return render(request,'exclui_fornecedor.html',dados)
#USUARIOS#
def lista_usuarios(request):
    procura = request.GET.get('procura')
    if procura:
        usuario = Usuario.objects.filter(nome__icontains=procura)
    else:
        usuario = Usuario.objects.all()
    total = usuario.count

    dados = { 
        'usuarios' : usuario, 
        'total' : total, 
        'procura': procura,
        'porPagina': efetua_paginacao(request, usuario) 
        }
    return render(request,'lista_usuarios.html',dados)

def cadastra_usuario(request):
    if request.method == 'POST':
        form = FormUsuario(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_usuarios)
    return render(request,'cadastra_usuario.html')

def altera_usuario(request,id):
    usuario = Usuario.objects.get(id=id)
    form = FormUsuario(request.POST, instance=usuario)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_usuarios)
            
    return render(request,'altera_usuario.html',{ 'usuario' : usuario })

def exclui_usuario(request, id):
    usuario = Usuario.objects.get(id=id)

    if request.method == 'POST':
        usuario.delete()
        return redirect(lista_usuarios)
    return render(request,'exclui_usuario.html', {'usuario':usuario})