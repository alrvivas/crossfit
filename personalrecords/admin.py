from django.contrib import admin
from .models import Personal_Record

@admin.register(Personal_Record)
class Personal_RecordAdmin(admin.ModelAdmin):
	list_display 	= ('id','cliente','ejercicio','pr')