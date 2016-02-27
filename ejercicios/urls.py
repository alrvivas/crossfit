from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'ejercicios.views.ejercicios', name='ejercicios'),	
	url(r'^perfil/(?P<ejercicio_id>[-\w]+)$', 'ejercicios.views.ejercicio', name='ejercicio'),
	url(r'^add-ejercicio/$', 'ejercicios.views.add_ejercicio', name='add-ejercicio'),
	url(r'^editar-ejercicio/(?P<ejercicio_id>[-\w]+)$', 'ejercicios.views.edit_ejercicio', name='editar-ejercicio'),
	
)