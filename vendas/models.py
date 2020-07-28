from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator
from clientes.models import Cliente
from decimal import Decimal


class Venda(models.Model):
   


    valor_total = models.DecimalField(max_digits=13, decimal_places=2, validators=[
                                     MinValueValidator(Decimal('0.00'))], null=True, blank=True)
    
    descricao_venda = models.TextField()
    data_compra = models.DateField(default=datetime.now)
    data_vencimento = models.DateField(default=datetime.now)
    cliente = models.ForeignKey(Cliente , on_delete=models.CASCADE, related_name='vendas')
    status = models.CharField(max_length=10,default='Andamento')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.cliente.nome


class parcelas(models.Model):
   venda = models.ForeignKey(Venda , on_delete=models.CASCADE, related_name='parcela_vendas')
   valor = models.FloatField()
   data = models.DateField(default=datetime.now)
   
   def __str__(self):
       return self.venda.descricao_venda # TODO
