from django.shortcuts import render, get_object_or_404, redirect
from .models import cliente
from .forms import ClienteForm

def inicio(request):
    return render(request, 'inicio.html')


def lista_clientes(request):
    clientes = cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/form_cliente.html', {'form': form})


def actualizar_cliente(request, pk):
    cliente_instance = get_object_or_404(cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente_instance)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente_instance)
    return render(request, 'clientes/form_cliente.html', {'form': form})

def eliminar_cliente(request, pk):
    cliente_instance = get_object_or_404(cliente, pk=pk)
    if request.method == 'POST':
        cliente_instance.delete()
        return redirect('lista_clientes')
    return render(request, 'clientes/confirmar_eliminar.html', {'objeto': cliente_instance})
