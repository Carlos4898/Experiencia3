from django.shortcuts import render, redirect
from .models import Gato
from .forms import GatoForm

# Create your views here.
def home(request):
    return render(request, 'Inicio.html')

def api(request):
    return render(request, 'ApiGatos.html')

def ayudanos(request):
    return render(request, 'Ayudanos.html')

def galeria(request):
    return render(request, 'GaleriaFotos.html')

def gatos(request):
    return render(request, 'Gatos.html')

def quienes(request):
    return render(request, 'QuienesSomos.html')

def mostrar(request):
    gato = Gato.objects.all()
    datos={
        'mininos':gato
    }
    #devolvemos a un template el diccionario y su contenido
    return render(request, 'mostrar.html', datos)
    
def eliminar(request, id):
    gato = Gato.objects.get(chip=id)
    gato.delete()
    return redirect('mostrar')



def crear(request):
    if request.method=='POST': 
        gatoform = GatoForm(request.POST)
        if gatoform.is_valid():
            gatoform.save()     #similar al insert
            return redirect('mostrar')
    else:
        gatoform=GatoForm()
    return render(request, 'crearGato.html', {'gatoform': gatoform}) 


def modificar(request, id):
    gato = Gato.objects.get(chip=id) #buscamos el objeto x patente = id
    datos ={
        'form': GatoForm(instance=gato) #instanciamos el obj. en un obj. de tipo formulario
    }
    #el siguiente bloque modifica el contenido del objeto almacenado
    if request.method=='POST':
        formulario = GatoForm(data=request.POST, instance=gato)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar')
    
    return render(request, 'modificar.html', datos)
