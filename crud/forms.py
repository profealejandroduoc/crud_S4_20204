from django import forms
from .models import Persona


class PersonaForm(forms.ModelForm):
    rut=forms.CharField(max_length=10, required=True)
    f_nacto=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    
    class Meta:
        model = Persona
        fields = ['rut','nombre','apellido','f_nacto','email','imagen']

