from django.contrib import admin
from .models import Orden, Tipo_Pago, Tipo_Abono, Estatus_Orden,Estatus_Cobranza,Orden_Producto

@admin.register(Estatus_Orden)
class Estatus_OrdenAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre',)

@admin.register(Estatus_Cobranza)
class Estatus_CobranzaAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre',)

@admin.register(Tipo_Pago)
class Tipo_PagoAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre',)

@admin.register(Tipo_Abono)
class Tipo_AbonoAdmin(admin.ModelAdmin):
	list_display 	= ('id','nombre',)

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
	list_display 	= ('id','cliente','estatus_orden','total_peso','total')