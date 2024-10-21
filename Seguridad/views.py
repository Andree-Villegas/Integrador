from django.shortcuts import render, redirect
from .models import Usuario  # Asegúrate de que 'Usuario' es tu modelo correcto

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contrasena = request.POST.get('password')

        if email and contrasena:
            try:
                # Verificar el usuario en la base de datos sin asignar a una variable
                Usuario.objects.get(email=email, contrasena=contrasena)
                # Redirigir a la selección de modo
                return redirect('modo')
            except Usuario.DoesNotExist:
                # Si no existe el usuario, mostrar error
                return render(request, 'login.html', {'error': 'Correo o contraseña incorrectos.'})

    return render(request, 'login.html')

def modo_view(request):
    return render(request, 'modo.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def trabajadores_view(request):
    return render(request, 'trabajadores.html')

def clientes_view(request):
    return render(request, 'clientes.html')

def serviciopremium_view(request):
    return render(request, 'serviciopremium.html')

def dashboardseguridad_view(request):
    return render(request, 'dashboardseguridad.html')

def usuarios_view(request):
    return render(request, 'usuario.html')

def nuevousuario_view(request):
    return render(request, 'nuevousuario.html')

def tokens_view(request):
    return render(request, 'tokens.html')

def monitoreo_view(request):
    return render(request, 'monitoreo.html')

def nuevotrabajador_view(request):
    return render(request, 'nuevotrabajador.html')

def nuevocomprador_view(request):
    return render(request, 'nuevocomprador.html')

def perfil_view(request):
    return render(request, 'perfil.html')
