from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$','producto.views.categorias', name='categorias'),
	url(r'^categorias/$', 'producto.views.ver_categoria', name='categorias'),
	url(r'^add-categoria/$', 'producto.views.add_categoria', name='add-categoria'),
	url(r'^categoria/(?P<categoria_slug>[-\w]+)/$','productos.views.ver_categoria', name='categoria'), 
	url(r'^producto/(?P<producto_slug>[-\w]+)/$','productos.views.producto', name='producto'),
	#url(r'^inventario/$', 'productos.views.inventario', name='inventario'),
	#url(r'^rescatar-inventario/$', 'productos.views.rescatar_inventario', name='rescatar-inventario'),

)