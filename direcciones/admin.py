from django.contrib import admin
from .models import Direccion

@admin.register(Direccion)
class DireccionkAdmin(admin.ModelAdmin):
	list_display 	= ('id','cliente','nombre')
