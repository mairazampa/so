from django.db import models


class Proceso(models.Model):
    
    nombre = models.CharField(max_length=20)
    arribo = models.IntegerField()
    duracion = models.IntegerField()
    memoria = models.IntegerField()
    tiempo_retorno = models.IntegerField()

    def __str__(self):
        return self.nombre


class Estrategia(models.Model):
    
    nombre = models.CharField(max_length=50)
    id = models.IntegerField()
    

    def __str__(self):
        return self.nombre

class Numero(models.Model):
    numbero = models.IntegerField()
    
class Memoria(models.Model):
    tamano = models.IntegerField()
    id_estrategia = models.ForeignKey(Estrategia, on_delete=models.CASCADE)
    tiempo_carga = models.IntegerField()
    tiempo_liberacion= models.IntegerField()
    tiempo_seleccion = models.IntegerField()
    id_proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE, related_name = "id_numero")
    id_numero = models.ForeignKey(Numero, on_delete = models.CASCADE, related_name = "id_proceso")

    def __str__(self):
        return self.nombre
