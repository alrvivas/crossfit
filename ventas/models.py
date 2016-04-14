#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from cliente.models import Cliente
from productos.models import *
from django.db.models import Count, Avg,Sum


class Tipo_Pago(models.Model):
    nombre = models.CharField(max_length=140)

    def __unicode__(self):
        return unicode(self.nombre)

class Tipo_Abono(models.Model):
    nombre = models.CharField(max_length=140)

    def __unicode__(self):
        return unicode(self.nombre)


class Estatus_Orden(models.Model):
    nombre = models.CharField(max_length=140)

    def __unicode__(self):
        return unicode(self.nombre)


class Estatus_Cobranza(models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.nombre)


class Orden(models.Model):
    cliente = models.ForeignKey(Cliente, null=True, blank=True)
    estatus_orden = models.ForeignKey(Estatus_Orden, null=True, blank=True)
    tipo_pago = models.ForeignKey(Tipo_Pago,null=True,blank=True)
    tipo_abono = models.ForeignKey(Tipo_Abono,null=True,blank=True)
    estatus_cobranza = models.ForeignKey(Estatus_Cobranza, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fehca_modificacion = models.DateTimeField(auto_now=True,verbose_name=('Ultima Modificacion'))
    comision_leche = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    total_peso = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    observacion = models.TextField(null=True,blank=True)

    @models.permalink
    def get_absolute_url(self):
        return('orden', (), { 'orden_id': self.id })

    @models.permalink
    def get_absolute_urlo(self):
        return('orden-pendiente', (), { 'orden_id': self.id })

    @models.permalink
    def get_absolute_urle(self):
        return('orden-exitosa', (), { 'orden_id': self.id })

    @models.permalink
    def get_absolute_url_corregir(self):
        return('corregir-orden', (), { 'orden_id': self.id })

    @models.permalink
    def get_absolute_url_revision(self):
        return('orden-revision', (), { 'orden_id': self.id })

    @models.permalink
    def get_absolute_url_pagada(self):
        return('orden-pagada', (), { 'orden_id': self.id })

    @models.permalink
    def get_absolute_url_adeudo(self):
        return('orden-adeudo', (), { 'orden_id': self.id })

    def __unicode__(self):
        return unicode(self.id)

    class Meta(object):
        verbose_name = ('Orden')
        verbose_name_plural = ('Ordenes')


class Orden_Producto(models.Model):
    orden = models.ForeignKey(Orden, null=True, blank=True,verbose_name='Orden Producto')
    producto = models.ForeignKey(Producto, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)
    subtotal_producto = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    subtotal_peso = models.DecimalField(max_digits=30, decimal_places=3, null=True, blank=True)

    def __unicode__(self):
        return u"%s - %s"% (self.orden, self.producto)
