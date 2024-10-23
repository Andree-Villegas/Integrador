from django.shortcuts import render, redirect
from .models import Usuario, Trabajador  
from .forms import TrabajadorForm
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        contrasena = request.POST.get('password')

        if email and contrasena:
            try:
                Usuario.objects.get(email=email, contrasena=contrasena)
                return redirect('modo')
            except Usuario.DoesNotExist:
                return render(request, 'login.html', {'error': 'Correo o contraseña incorrectos.'})

    return render(request, 'login.html')

def modo_view(request):
    return render(request, 'modo.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def trabajadores_view(request):
    trabajadores = Trabajador.objects.all()
    return render(request, 'trabajadores.html', {'trabajadores': trabajadores})

def nuevotrabajador_view(request):
    if request.method == 'POST':
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        numtarjeta = request.POST.get('numtarjeta')
        email = request.POST.get('email')
        numtelefono = request.POST.get('numtelefono')

        trabajador = Trabajador(nombres=nombres, apellidos=apellidos, numtarjeta=numtarjeta, email=email, numtelefono=numtelefono)
        trabajador.save()  # Guarda el trabajador manualmente
        print("Trabajador guardado correctamente")
        return redirect('trabajadores')  # Redirige a la lista de trabajadores
    return render(request, 'nuevotrabajador.html')

def editar_trabajador(request, id):
    trabajador = Trabajador.objects.get(IDtrabajador=id)  # Obtiene el trabajador por ID
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()  # Guarda los cambios en la base de datos
            return redirect('trabajadores')  # Redirige de nuevo a la página de trabajadores
    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, 'editar_trabajador.html', {'form': form})

def eliminar_trabajador(request, id):
    trabajador = Trabajador.objects.get(IDtrabajador=id)
    trabajador.delete()
    return redirect('trabajadores')

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

def nuevocomprador_view(request):
    return render(request, 'nuevocomprador.html')

def perfil_view(request):
    return render(request, 'perfil.html')
