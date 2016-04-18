from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'ventas.views.punto_venta', name='punto-venta'),
	url(r'^ordenes-exitosa/(?P<orden_id>[-\w]+)$', 'ventas.views.orden_exitosa', name='orden-exitosa'),
	url(r'^orden/(?P<orden_id>[-\w]+)$', 'ventas.views.orden', name='orden'),
	url(r'^credito-cobranza/', 'ventas.views.credito_cobranza', name='credito-cobranza'),	
	
)