from django.db import models
from django.contrib.auth.models import User

class Ejercicio(models.Model):
	nombre = models.CharField(max_length=140,null=True)
	descripcion = models.TextField(null=True)

	def __unicode__(self):
		return unicode(self.nombre)