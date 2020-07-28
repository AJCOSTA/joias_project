from django.shortcuts import render
from .models import Venda

def newSale(request):
   vendas = Venda()
   return render(request, 'vendas/venda.html',{'vendas': vendas})
