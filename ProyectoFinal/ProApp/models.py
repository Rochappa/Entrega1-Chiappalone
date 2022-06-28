from django.db import models

class Autos(models.Model):

    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    anio = models.IntegerField()
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Año: {self.anio} - Color: {self.color}"

class Motos(models.Model):

    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    cilindrada = models.IntegerField()
    anio = models.IntegerField()

    def __str__(self):
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Cilindrada: {self.cilindrada} Año: {self.anio}"

class Camiones(models.Model):

    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    anio = models.IntegerField()
    carga_total = models.IntegerField()

    def __str__(self):
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Año: {self.anio} - Capacidad de Carga: {self.carga_total}"

