from django.shortcuts import render

# Create your views here.
def produtos(request):
    return render(request,'lista_produtos.html')