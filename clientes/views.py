from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import ClienteForm

from django.contrib import messages

@login_required
def clienteList(request):

    search = request.GET.get('search')
    filter = request.GET.get('filter')
    # tasksDoneRecently = Task.objects.filter(done='done', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30)).count()
    # tasksDone = Task.objects.filter(done='done', user=request.user).count()
    # tasksDoing = Task.objects.filter(done='doing', user=request.user).count()

    if search:

        clientes = Cliente.objects.filter(CPF__icontains=search)
        
    elif filter:

        clientes = Cliente.objects.filter(status=filter)
        

    else:


        clientes_list = Cliente.objects.all().order_by('-created_at')

        paginator = Paginator(clientes_list, 5)

        page = request.GET.get('page')

        clientes = paginator.get_page(page)

    return render(request, 'clientes/list.html',{'clientes': clientes})
@login_required
def clienteView(request, id):
    cliente = get_object_or_404(Cliente, pk=id)     
    return render(request,'clientes/cliente.html',{'cliente': cliente})

@login_required
def newCliente(request):
    
    form = ClienteForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            form.save()
           
            return redirect('/')


    
    return render(request, 'clientes/addcliente.html', {'form': form})

@login_required
def editCliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClienteForm(instance=cliente)

    if(request.method == 'POST'):
        form = ClienteForm(request.POST, instance=cliente)

        if(form.is_valid()):
            cliente.save()
            return redirect('/')
        
        else:
            return render(request, 'clientes/editcliente.html', {'form': form, 'cliente': cliente})
    else:
        return render(request, 'clientes/editcliente.html', {'form': form, 'cliente': cliente})


@login_required
def deleteCliente(request, id):
     cliente = get_object_or_404(Cliente, pk=id)
     cliente.delete()
     messages.info(request, 'Cliente deletado com Sucesso!')
     return redirect('/')


     



