from django.contrib import admin
from .models import Persona,Mascota, User

# Register your models here.
class AdmPersona(admin.ModelAdmin):
        list_display=['rut','nombre','apellido','f_nacto','email','imagen']

class AdmMascota(admin.ModelAdmin):
    list_display=['id','nombre','edad','tipo','subtipo','propietario']
    list_editable=['nombre','edad','tipo','subtipo','propietario']
    list_filter=['propietario','edad','tipo']


admin.site.register(Persona, AdmPersona)
admin.site.register(Mascota,AdmMascota)
admin.site.register(User)