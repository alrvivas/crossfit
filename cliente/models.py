from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Cliente(models.Model):
	fecha_registro = models.DateField(null=True)	
	nombre = models.CharField(max_length=140,null=True)
	apellidos = models.CharField(max_length=140,null=True)
	celular	= models.CharField(max_length=15,null=True)
	telefono = models.CharField(max_length=15,null=True)
	dias_credito = models.PositiveIntegerField(null=True)	
	imagen = models.ImageField("Imagen Cliente", upload_to="images/clientes", blank=True, null=True,default='images/clientes/default-01.jpg')
	
	@models.permalink
	def get_absolute_url(self):
		return('cliente', (), { 'cliente_id': self.id })
		
	@models.permalink
	def get_absolute_url_edit_e(self):
		return('editar-cliente', (), { 'cliente_id': self.id })

	@models.permalink
	def get_absolute_url_ordenes_pendientes_cliente(self):
		return('ordenes-pendientes-cliente', (), { 'cliente_id': self.id })

	@models.permalink
	def get_absolute_url_ordenes_pagadas_cliente(self):
		return('ordenes-pagadas-cliente', (), { 'cliente_id': self.id })

	def __unicode__(self):
		return unicode(self.nombre)

