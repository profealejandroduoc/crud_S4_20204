from django import forms
from .models import Persona, User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    pass
    class Meta:
        model=User
        fields=['rut','username','first_name','last_name','email','direccion','password1','password2']



class PersonaForm(forms.ModelForm):
    rut=forms.CharField(max_length=10, required=True)
    f_nacto=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    
    class Meta:
        model = Persona
        fields = ['rut','nombre','apellido','f_nacto','email','imagen']
        

class UpdPersonaForm(forms.ModelForm):
    
    f_nacto=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    
    class Meta:
        model = Persona
        fields = ['nombre','apellido','f_nacto','email','imagen']

