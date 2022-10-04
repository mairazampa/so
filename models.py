from django.db import models

# Create your models here.
class Procesos(models.Model):
    
    nombre = models.CharField(max_length=20)
    arribo = models.IntegerField()
    duracion = models.IntegerField()
    memoria = models.IntegerField()
    tiempo_retorno = models.IntegerField()

    def __str__(self):
        return self.nombre


class Estrategia(models.Model):
    
    nombre = models.CharField(max_length=20)
    id = models.IntegerField()
    

    def __str__(self):
        return self.nombre

class Memoria(models.Model):
    tamano = models.IntegerField()
    id_estrategia = models.ForeignKey(Estrategia, on_delete=models.CASCADE)
    tiempo_carga = models.IntegerField()
    tiempo_liberacion= models.IntegerField()
    tiempo_seleccion = models.IntegerField()

    def __str__(self):
        return self.nombre