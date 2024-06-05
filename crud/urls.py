from django.urls import path

from .views import index, personas,pasadatos


urlpatterns = [
    path('',index,name="index"),
    path('personas/', personas, name='personas'),
    path('pasadatos/',pasadatos,name='pasadatos')
]
