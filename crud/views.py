from django.shortcuts import render
from datetime import date, datetime
from .models import Persona
from django.shortcuts import get_object_or_404, redirect
from .forms import PersonaForm

# Create your views here.
def index(request):
    return render(request,'crud/index.html')


def personas(request):
    personas=Persona.objects.all()
    
    datos={
        "personas":personas
    }

    return render(request,'crud/personas.html', datos)

def pasadatos(request):
    fecha=datetime.now()
    mensaje="Mensaje desde la vista"
    lista=["perro","gato","raton"]
    numero=10
    
    datos={
        "fecha":fecha,
        "msg":mensaje,
        "animales":lista,
        "numero":numero
    }
    
    print(f"La fecha de hoy es {fecha}")
    return render(request,'crud/pasadatos.html', datos)

def detalles(request, id):
    
    #persona=Persona.objects.get(rut=id)
    persona=get_object_or_404(Persona,rut=id)
    
    datos={
        "persona":persona
    }
    return render(request,'crud/detalles.html',datos)


def crearpersona(request):
    
    formulario=PersonaForm()

    if request.method=="POST":
        formulario=PersonaForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="personas")
        
    datos={
        "formulario":formulario
    }

    return render(request,'crud/crearpersona.html', datos)