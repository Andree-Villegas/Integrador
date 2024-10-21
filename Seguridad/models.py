from django.db import models

class Usuario(models.Model):
    IDusuario = models.AutoField(primary_key=True)  # Clave primaria
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)

    class Meta:
        db_table = 'usuario'  # Especifica el nombre exacto de la tabla en tu base de datos

    def __str__(self):
        return self.email  # Mostrar el email como representación de usuario
