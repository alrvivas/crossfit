from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'ventas.views.punto_venta', name='punto-venta'),
	url(r'^orden/(?P<orden_id>[-\w]+)$', 'ventas.views.orden', name='orden'),
	url(r'^ordenes-exitosa/(?P<orden_id>[-\w]+)$', 'ventas.views.orden_exitosa', name='orden-exitosa'),	
	url(r'^editar-orden/(?P<orden_id>[-\w]+)$', 'ventas.views.editar_orden', name='editar-orden'),
	url(r'^credito-cobranza/', 'ventas.views.credito_cobranza', name='credito-cobranza'),
	url(r'^corregir-orden/(?P<orden_id>[-\w]+)$', 'ventas.views.corregir_orden', name='corregir-orden'),
	url(r'^abonar-orden/(?P<orden_id>[-\w]+)$', 'ventas.views.abonar_orden', name='abonar-orden'),	
	url(r'^crear-devolucion/$', 'ventas.views.crear_devolucion', name='crear-devolucion'),
	url(r'^devolucion-exitosa/(?P<devolucion_id>[-\w]+)$', 'ventas.views.devolucion_exitosa', name='devolucion-exitosa'),
	
)