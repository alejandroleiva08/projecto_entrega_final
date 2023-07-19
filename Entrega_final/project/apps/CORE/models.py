from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
#    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
#    estudiantes = models.ManyToManyField(Estudiante)
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    caracteristica = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    edad = models.IntegerField()
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre




