from django.contrib import admin
from .models import Ejercicio

@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre','descripcion')