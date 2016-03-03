from django.db import models
from django.contrib.auth.models import User
from cliente.models import *
from ejercicios.models import *

class Personal_Record(models.Model):
	cliente = models.ForeignKey(Cliente,null=True)
	ejercicio = models.ForeignKey(Ejercicio,null=True)
	fecha = models.DateField(null=True)
	pr = models.CharField(max_length=20,null=True)

	def __unicode__(self):
		return unicode(self.id)


	@models.permalink
	def get_absolute_url(self):
		return('recor-personal', (), { 'recordpersona_id': self.id })

	@models.permalink
	def get_absolute_url_edit_pr(self):
		return('editar-recor-personal', (), { 'recordpersona_id': self.id })