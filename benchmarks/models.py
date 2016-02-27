from django.db import models
from django.contrib.auth.models import User
from cliente.models import *
from ejercicios.models import *

class Benchmark(models.Model):
	nombre = models.CharField(max_length=50,null=True)	
	tiempo = models.PositiveIntegerField(null=True)	
	tiempo_pr = models.PositiveIntegerField(null=True)
	repeticiones_pr = models.PositiveIntegerField(null=True)

	def __unicode__(self):
		return unicode(self.nombre)

class Ejercicio_Benchmark(models.Model):	
	benchmark = models.ForeignKey(Benchmark,null=True)
	ejercicio = models.ForeignKey(Ejercicio,null=True)
	repeticiones = models.PositiveIntegerField(null=True)

	def __unicode__(self):
		return unicode(self.nombre)