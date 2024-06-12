from django.urls import path

from .views import index, personas,pasadatos,detalles, crearpersona,modificarpersona, eliminarpersona

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',index,name="index"),
    path('personas/', personas, name='personas'),
    path('pasadatos/',pasadatos,name='pasadatos'),
    path('detalles/<id>',detalles, name='detalles'),
    path('crearpersona/',crearpersona,name='crearpersona'),
    path('modificarpersona/<id>',modificarpersona, name='modificarpersona'),
    path('eliminarpersona/<id>',eliminarpersona,name='eliminarpersona')
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
