from django.db import models

# Create your models here.
class Carro(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField(default=1)
    año = models.IntegerField(default=20)
