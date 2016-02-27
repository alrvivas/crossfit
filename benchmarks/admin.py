from django.contrib import admin
from .models import Benchmark,Ejercicio_Benchmark

@admin.register(Benchmark)
class BenchmarkAdmin(admin.ModelAdmin):
	list_display 	= ('id','tiempo','tiempo_pr','repeticiones_pr')

@admin.register(Ejercicio_Benchmark)
class Ejercicio_BenchmarkAdmin(admin.ModelAdmin):
	list_display 	= ('id','benchmark','ejercicio','repeticiones')

