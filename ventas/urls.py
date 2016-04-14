from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'ventas.views.punto_venta', name='punto-venta'),
	url(r'^ordenes-exitosa/$', 'ventas.views.orden_exitosa', name='orden-exitosa'),	
	
)