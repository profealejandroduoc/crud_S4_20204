from django.shortcuts import render
from datetime import date, datetime
from .models import Persona
from django.shortcuts import get_object_or_404, redirect
from .forms import PersonaForm, UpdPersonaForm
from django.contrib import messages

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
            #from django.contrib import messages
            messages.set_level(request,messages.SUCCESS)
            messages.success(request, "Persona creada con exito!!!")
            return redirect(to="personas")
        
    datos={
        "formulario":formulario
    }

    return render(request,'crud/crearpersona.html', datos)

def modificarpersona(request,id):
    persona=get_object_or_404(Persona, rut=id)
    form=UpdPersonaForm(instance=persona)
    
    
    if request.method=="POST":
         form=UpdPersonaForm(request.POST, files=request.FILES, instance=persona)
         if form.is_valid():
             form.save()
             messages.set_level(request,messages.WARNING)
             messages.warning(request,"Persona modificada")
             return redirect(to="personas")
    
    datos={
        'persona':persona,
        'form':form
    }
    return render(request,'crud/modificarpersona.html',datos)


def eliminarpersona(request,id):
    persona=get_object_or_404(Persona, rut=id)
 
    
    
    if request.method=="POST":
        persona.delete()
        return redirect(to="personas")
      

    
    datos={
        'persona':persona,
    
    }
    return render(request,'crud/eliminarpersona.html',datos)