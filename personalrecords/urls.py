from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'personalrecords.views.personalrecords', name='records-personales'),	
	url(r'^record-personal/(?P<recordpersona_id>[-\w]+)$', 'personalrecords.views.personal_record', name='record-personal'),
	url(r'^add-record-persoal/$', 'personalrecords.views.add_personal_record', name='add-record-persoal'),
	url(r'^editar-record-personal/(?P<recordpersona_id>[-\w]+)$', 'personalrecords.views.edit_personal_record', name='editar-record-personal'),
	
)