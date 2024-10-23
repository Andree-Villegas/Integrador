"""
URL configuration for Integrador project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tkinter.font import names
from django.urls import path
from Seguridad import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login')),  # Redirigir al login por defecto
    path('login/', views.login_view, name='login'),  # Ruta para el login
    path('modo/', views.modo_view, name='modo'),  # Ruta para seleccionar modo
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Ruta para el dashboard (modo cloud)
    path('trabajadores/', views.trabajadores_view, name='trabajadores'),  # Ruta para trabajadores
    path('clientes/', views.clientes_view, name='clientes'),  # Ruta para clientes
    path('serviciopremium/', views.serviciopremium_view, name='serviciopremium'),  # Ruta para servicio premium
    path('dashboardseguridad/', views.dashboardseguridad_view, name='dashboardseguridad'),  # Ruta para el dashboard de Seguridad
    path('usuario/', views.usuarios_view, name='usuario'),   #Ruta para ver el usuario.html
    path('tokens/', views.tokens_view, name='tokens'),
    path('monitoreo/', views.monitoreo_view, name='monitoreo'),
    path('nuevousuario/', views.nuevousuario_view, name='nuevousuario'),
    path('nuevotrabajador/', views.nuevotrabajador_view, name='nuevotrabajador'),
    path('nuevocomprador/', views.nuevocomprador_view, name='nuevocomprador'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('trabajador/editar/<int:id>/', views.editar_trabajador, name='editar_trabajador'),
    path('trabajador/eliminar/<int:id>/', views.eliminar_trabajador, name='eliminar_trabajador'),
]
