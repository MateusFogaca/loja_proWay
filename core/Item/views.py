from django.shortcuts import render, redirect
from ViewsProject.views import efetua_paginacao
from .forms import FormCategoria, FormItem
from .models import Categoria, Item

# Create your views here.
def lista_categorias(request):
    procura = request.GET.get('procura')

    if procura:
        categorias = Categoria.objects.filter(nome__icontains=procura)
    else:
        categorias = Categoria.objects.all()
    total = categorias.count

    dados = { 
        'categorias' : categorias, 
        'total' : total, 
        'procura': procura,
        'porPagina':efetua_paginacao(request, categorias)
        }
    return render(request,'lista_categorias.html',dados)

def cadastra_categoria(request):
    if request.method == 'POST':
        form = FormCategoria(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_categorias)
    return render(request,'cadastra_categoria.html')

def altera_categoria(request,id):
    categoria = Categoria.objects.get(id=id)
    form = FormCategoria(request.POST, instance=categoria)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_categorias)

    return render(request,'altera_categoria.html',{ 'categoria' : categoria })

def exclui_categoria(request, id):
    categoria = Categoria.objects.get(id=id)

    if request.method == 'POST':
        categoria.delete()
        return redirect(lista_categorias)
    return render(request,'exclui_categoria.html',{'categoria':categoria})
#ITENS#
def lista_itens(request):
    procura = request.GET.get('procura')
    if procura:
        item = Item.objects.filter(nome__icontains=procura)
    else:
        item = Item.objects.all()
    total = item.count

    dados = { 
        'item' : item, 
        'total' : total, 
        'procura': procura,
        'porPagina': efetua_paginacao(request, item)
        }
    return render(request,'lista_itens.html',dados)

def cadastra_item(request):
    categoria = Categoria.objects.all()
    if request.method == 'POST':
        form = FormItem(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(lista_itens)
    return render(request,'cadastra_item.html',{ 'categorias' : categoria })

def altera_item(request,id):
    item = Item.objects.get(id=id)
    categorias = Categoria.objects.all()
    categoriaItem = Categoria.objects.get(id=item.categoria_id)
    form = FormItem(request.POST, instance=item)

    dados = { 
            'item' : item, 
            'categoriaItem' : categoriaItem.id, 
            'categorias' : categorias 
            }            

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(lista_itens)

    return render(request,'altera_item.html',dados)

def exclui_item(request, id):
    item = Item.objects.get(id=id)
    categoria = Categoria.objects.get(id=item.categoria_id)

    if request.method == 'POST':
        item.delete()
        return redirect(lista_itens)
    return render(request,'exclui_item.html', {'item':item, 'categ':categoria})