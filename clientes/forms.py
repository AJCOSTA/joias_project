from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome', 'endereco', 'CPF', 'telefone','data_nascimento',  'status' , 'descricao')

