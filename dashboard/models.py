from django.db import models

class Tipos(models.Model):#Modelo de los tipos de puntos presentes en el mapa
    nombre = models.CharField(primary_key=True,max_length=150,unique=True)
    nombre_espanol = models.CharField(max_length=150,blank=True,null=True)
    def __str__(self):
        return str(self.nombre)
class Puntos(models.Model):#modelo de los puntos o markers
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    tipo = models.ForeignKey(Tipos, on_delete=models.CASCADE)

    def __str__(self):
        return str("Punto "+ str(self.nombre))
