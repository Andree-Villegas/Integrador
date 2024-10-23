from django import forms
from .models import Trabajador

#Formulario para el modelo "trabajador"
class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ['nombres', 'apellidos', 'numtarjeta', 'email', 'numtelefono']