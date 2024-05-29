from django.contrib import admin
from .models import Persona,Mascota

# Register your models here.


class AdmMascota(admin.ModelAdmin):
    list_display=['id','nombre','edad','tipo','subtipo','propietario']
    list_editable=['nombre','edad','tipo','subtipo','propietario']
    list_filter=['propietario','edad','tipo']


admin.site.register(Persona)
admin.site.register(Mascota,AdmMascota)