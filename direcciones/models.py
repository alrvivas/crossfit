from django.db import models
from django.contrib.auth.models import User
from cliente.models import *

class Estado(models.Model):
	nombre = models.CharField(max_length=140,null=True)

	def __unicode__(self):
		return unicode(self.nombre)

class Ciudad(models.Model):
	estado =  models.ForeignKey(Estado,null=True)
	nombre = models.CharField(max_length=140,null=True)

	def __unicode__(self):
		return unicode(self.nombre)

class Direccion(models.Model):
	cliente = models.ForeignKey(Cliente,null=True)
	nombre = models.CharField(max_length=140,null=True)
	calle = models.CharField(max_length=140,null=True)
	numero_exterior = models.CharField(max_length=12,null=True)
	numero_interior = models.CharField(max_length=12,null=True)
	colonia = models.CharField(max_length=140,null=True)
	cp = models.CharField(max_length=140,null=True)
	ciudad = models.ForeignKey(Ciudad,null=True)
