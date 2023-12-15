from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return f"Nombre: {self.nombre}"

class Distribuidor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre}, Telefono: {self.telefono}"
