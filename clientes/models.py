from django.db import models
from datetime import datetime


class Cliente(models.Model):

    STATUS = (
        ('ativo','ATIVO'),
        ('inativo','INATIVO'),

    )

    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    descricao = models.TextField()
    telefone = models.CharField(max_length=32)
    CPF = models.CharField(max_length=11,unique=True)
    data_nascimento = models.DateField(default=datetime.now)

    status = models.CharField(
        max_length=7,
        choices = STATUS, 
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.nome

    

