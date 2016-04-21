from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'almacenes.views.almacenes', name='almacenes'),	
	url(r'^almacen/(?P<almacen_id>[-\w]+)$', 'almacenes.views.almacen', name='almacen'),
	url(r'^add-almacen/$', 'almacenes.views.add_almacen', name='add-almacen'),
	url(r'^editar-almacen/(?P<almacen_id>[-\w]+)$', 'almacenes.views.edit_almacen', name='editar-almacen'),
)