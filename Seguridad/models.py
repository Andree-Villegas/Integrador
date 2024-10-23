from django.db import models

# Modelo Usuario
class Usuario(models.Model):
    IDusuario = models.AutoField(primary_key=True)  # Clave primaria
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)

    class Meta:
        db_table = 'usuario'  

    def __str__(self):
        return self.email  

# Modelo trabajador
class Trabajador(models.Model):
    IDtrabajador = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    numtarjeta = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=50)
    numtelefono = models.CharField(max_length=20)

    class Meta:
        db_table = 'trabajador'
        managed = False

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
