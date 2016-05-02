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
    def get_absolute_urle(self):
        return('orden-exitosa', (), { 'orden_id': self.id })

    @models.permalink
    def get_absolute_url_editar(self):
        return('editar-orden', (), { 'orden_id': self.id })

    @models.permalink
    def get_absolute_url_entregar(self):
        return('entregar-orden', (), { 'orden_id': self.id })

    @models.permalink
    def get_absolute_url_entrega_exitosa(self):
        return('entrega-orden-exitosa', (), { 'orden_id': self.id })

    @models.permalink
    def get_absolute_url_mandar_revision(self):
        return('mandar-revision-orden', (), { 'orden_id': self.id })

    @models.permalink
    def get_absolute_url_corregir(self):
        return('corregir-orden', (), { 'orden_id': self.id })

    @models.permalink
    def get_absolute_url_abonar_orden(self):
        return('abonar-orden', (), { 'orden_id': self.id })

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

class Abono(models.Model):
    orden = models.ForeignKey(Orden, null=True, blank=True,verbose_name='Orden')
    cantidad = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fehca_modificacion = models.DateTimeField(auto_now=True,verbose_name=('Ultima Modificacion'))

    def __unicode__(self):
        return unicode(self.nombre)


class Devoluvcion(models.Model):
    orden = models.ForeignKey(Orden, null=True, blank=True,verbose_name='Orden')    
    fecha = models.DateField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fehca_modificacion = models.DateTimeField(auto_now=True,verbose_name=('Ultima Modificacion'))
    subtotal = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    total_peso = models.DecimalField(max_digits=10, decimal_places=4, null=True)
    observacion = models.TextField(null=True,blank=True)

    @models.permalink
    def get_absolute_url(self):
        return('devoluvcion', (), { 'devolucion_id': self.id })

    @models.permalink
    def get_absolute_url_crear(self):
        return('crear-devolucion', (), { 'devolucion_id': self.id })

    @models.permalink
    def get_absolute_url_capturar(self):
        return('capturar-devolucion', (), { 'devolucion_id': self.id })

    @models.permalink
    def get_absolute_urle(self):
        return('devolucion-exitosa', (), { 'devolucion_id': self.id })

    @models.permalink
    def get_absolute_url_editar(self):
        return('editar-devolucion', (), { 'devolucion_id': self.id })

    def __unicode__(self):
        return unicode(self.id)

    class Meta(object):
        verbose_name = ('Devolucion')
        verbose_name_plural = ('Devoluciones')



class Devoluvcion_Producto(models.Model):
    devoluvcion = models.ForeignKey(Devoluvcion, null=True, blank=True,verbose_name='Orden Producto')
    producto = models.ForeignKey(Producto, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    cantidad = models.IntegerField(null=True, blank=True)
    subtotal_producto = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    subtotal_peso = models.DecimalField(max_digits=30, decimal_places=3, null=True, blank=True)

    def __unicode__(self):
        return u"%s - %s"% (self.orden, self.producto)