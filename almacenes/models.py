from django.db import models
from django.contrib.auth.models import User

class Almacen(models.Model):
	fecha_registro = models.DateTimeField(auto_now_add=True,verbose_name=('Fecha de Creacion'))
	fehca_modificacion = models.DateTimeField(auto_now=True,verbose_name=('Ultima Modificacion'))	
	nombre = models.CharField(max_length=140,null=True)
	celular	= models.CharField(max_length=15,null=True)
	telefono = models.CharField(max_length=15,null=True)	
	
	@models.permalink
	def get_absolute_url(self):
		return('almacen', (), { 'almacen_id': self.id })		
	

	def __unicode__(self):
		return unicode(self.nombre)

