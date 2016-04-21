from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'cliente.views.clientes', name='clientes'),	
	url(r'^perfil/(?P<cliente_id>[-\w]+)$', 'cliente.views.cliente', name='cliente'),
	url(r'^add-cliente/$', 'cliente.views.add_cliente', name='add-cliente'),
	url(r'^editar-cliente/(?P<cliente_id>[-\w]+)$', 'cliente.views.edit_cliente', name='editar-cliente'),
	url(r'^ordenes-pendientes-cliente/(?P<cliente_id>[-\w]+)$', 'cliente.views.ordenes_pendientes_cliente', name='ordenes-pendientes-cliente'),
	url(r'^ordenes-pagadas-cliente/(?P<cliente_id>[-\w]+)$', 'cliente.views.ordenes_pagadas_cliente', name='ordenes-pagadas-cliente'),
	
)