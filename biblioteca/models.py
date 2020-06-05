from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return str (self.nombre)

class Libro (models.Model):
    autor = models.ForeignKey('Autor', null = False, on_delete = models.CASCADE)
    titulo = models.CharField(max_length = 50)
    paginas = models.IntegerField()
    editorial = models.CharField(max_length = 50)
    def __str__(self):
        return str (self.titulo)


class Ejemplar (models.Model):
    localizacion = models.CharField(max_length = 50)
    libro = models.ForeignKey('Libro', null = False, on_delete = models.CASCADE)
    def __str__(self):
        return str (self.localizacion + " " + self.libro.titulo)

class Usuario (models.Model):
    nombre = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=50, null=False)
    direccion = models.CharField(max_length=50, null=False)
    ejemplares = models.ManyToManyField(Ejemplar)
    def __str__ (self):
        return str (self.nombre)