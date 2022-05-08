from unicodedata import name
from django.urls import path
from . import views
from django.contrib import admin

import mainSistema.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('', mainSistema.views.visitante, name='visitante'),
    path('visitante/', mainSistema.views.visitante, name='visitante'),
    path('ingreso/', mainSistema.views.ingreso, name='ingreso'),
    path('', mainSistema.views.dispositivos, name='dispositivos'),
    path('dispositivos/', mainSistema.views.dispositivos, name='dispositivos'),
    path('', mainSistema.views.puntos_de_control, name='puntos_de_control'),
    path('puntos_de_control/', mainSistema.views.puntos_de_control, name='puntos_de_control'),
    path('', views.permisos, name='permisos'),
    path('permisos/', views.permisos, name='permisos'),
    path('', views.reporte_visitante, name='reporte_visitante'),
    path('reporte_visitante/', views.reporte_visitante, name='reporte_visitante'),
    path('', views.generar_QR, name='generar_QR'),
    path('generar_QR/', views.generar_QR, name='generar_QR'),
    path('save/', views.save_visitante, name="save"),
    path('pruebas-orm/', views.pruebas_orm, name="pruebas-orm"),
  

  
]  

