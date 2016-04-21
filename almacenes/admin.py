from django.contrib import admin
from .models import Almacen

@admin.register(Almacen)
class AlmacennAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre',)
