from django.shortcuts import render, redirect
from .forms import FormCidade, FormEstado
from .models import Estado, Cidade

# Create your views here.
def lista_estados(request):
    procura = request.GET.get('procura')
    if procura:
        estado = Estado.objects.filter(sigla__icontains=procura)|Estado.objects.filter(nome__icontains=procura)
    else:
        estado = Estado.objects.all()
    total = estado.count
    return render(request,'lista_estados.html',{'estado' : estado, 'total' : total, 'procura': procura })

def cadastra_estado(request):
    if request.method == 'POST':
        form = FormEstado(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_estados)
    return render(request,'cadastra_estado.html')

def altera_estado(request,id):
    estado = Estado.objects.get(id=id)
    form = FormEstado(request.POST, instance=estado)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_estados)

    return render(request,'altera_estado.html',{ 'estado' : estado })

def exclui_estado(request, id):
    estado = Estado.objects.get(id=id)

    if request.method == 'POST':
        estado.delete()
        return redirect(lista_estados)
    return render(request,'exclui_estado.html',{'estado': estado})

def lista_cidades(request):
    procura = request.GET.get('procura')
    if procura:
        cidades = Cidade.objects.filter(nome__icontains=procura)
    else:
        cidades = Cidade.objects.all()
    total = cidades.count
    return render(request,'lista_cidades.html', { 'cidades' : cidades, 'total' : total, 'procura': procura })

def cadastra_cidade(request):
    estado = Estado.objects.all()
    if request.method == 'POST':
        form = FormCidade(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_cidades)
    return render(request,'cadastra_cidade.html', { 'estados' : estado })

def altera_cidade(request,id):
    cidade = Cidade.objects.get(id=id) # SELECT * FROM cidades WHERE id = id
    estados = Estado.objects.all() # SELECT * FROM estados
    estadoId = Estado.objects.get(id=cidade.estado_id) # Já sei qual é o Estado da cidade selecionada
    form = FormCidade(request.POST, instance=cidade)
    dados = {
        'cidade' : cidade,
        'estados' : estados,
        'estadoId' : estadoId.id
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_cidades)
    return render(request,'altera_cidade.html',dados)

def exclui_cidade(request, id):
    cidade = Cidade.objects.get(id=id)
    estado = Estado.objects.get(id=cidade.estado_id)

    if request.method == 'POST':
        cidade.delete()
        return redirect(lista_cidades)
    return render(request,'exclui_cidade.html',{'cidade':cidade, 'estado': estado})