from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)), 
    url(r'^$', 'cliente.views.index', name='index'),	
	url(r'^login/$', 'cliente.views.LoginView', name='login'),
    url(r'^logout/$', 'cliente.views.LogoutView', name='logout'), 
    url(r'^clientes/', include('cliente.urls')),
    url(r'^ejercicios/', include('ejercicios.urls')),
    url(r'^records-personales/', include('personalrecords.urls')),
    url(r'^productos/', include('productos.urls')),
    url(r'^ventas/', include('ventas.urls')),
    #url(r'^almacenes/', include('almacenes.urls')),      
)   

 
if settings.DEBUG == False:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
   )