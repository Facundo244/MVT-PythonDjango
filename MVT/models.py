from django.db import models

class Familiar1(models.Model):

    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    fechaDeNacimiento = models.DateField()
    anios = models.IntegerField()

class Familiar2(models.Model):

    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    fechaDeNacimiento = models.DateField()
    anios = models.IntegerField()


class Familiar3(models.Model):

    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    fechaDeNacimiento = models.DateField()
    anios = models.IntegerField()





