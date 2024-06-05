from django.shortcuts import render
from datetime import date, datetime
from .models import Persona

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