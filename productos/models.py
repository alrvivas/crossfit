from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length=140, verbose_name=('Nombre Categoria'))
	slug = models.SlugField(max_length=50, unique=True, help_text='Valor unico por producto URL pagina, creado desde nombre.',blank=True,null=True)
	activo = models.BooleanField(default=True)
	orden = models.PositiveIntegerField(null=True, blank=True)
	imagen = models.ImageField("Imagen Categoria", upload_to="images/producto/categorias", blank=True, null=True,default='images/producto/categorias/default-01.png')

	def imagen_categoria(self):
		return """<img src="%s" style="width:8em;" />""" % self.imagen.url

	imagen_categoria.allow_tags = True

	class Meta:
		ordering = ['orden']
		verbose_name_plural = 'Categorias' 

	def __unicode__(self): 
		return self.nombre

	@models.permalink
	def get_absolute_url(self):
		return ('categoria', (), { 'categoria_slug': self.slug })

class Producto(models.Model):
	categoria = models.ForeignKey(Categoria)
	nombre = models.CharField(max_length=255, verbose_name=('Nombre'))
	slug = models.SlugField(verbose_name=('Slug'), unique=True,null=True, blank=True)
	activo = models.BooleanField(default=False, verbose_name=('Activo'))
	codigo_barras = models.CharField(max_length=20, unique=True,null=True, blank=True)	
	vida_anaquel = models.IntegerField(blank=True)
	fecha_registro = models.DateTimeField(auto_now_add=True,verbose_name=('Fecha de Creacion'))
	fehca_modificacion = models.DateTimeField(auto_now=True,verbose_name=('Ultima Modificacion'))
	orden = models.PositiveIntegerField()
	stock = models.IntegerField(null=True, blank=True)
	precio_unitario = models.DecimalField(max_digits = 30,decimal_places = 3,verbose_name=('Precio'))
	presentacion = models.CharField(max_length=50,null=True, blank=True)
	unidad = models.IntegerField(blank=True, default=1)
	peso = models.DecimalField(max_digits = 30,decimal_places = 3,)
	imagen = models.ImageField("Imagen Categoria", upload_to="images/producto", blank=True, null=True,default='images/producto/default-01.png')


	class Meta(object):
		ordering = ['categoria','orden']
		verbose_name = ('Producto')
		verbose_name_plural = ('Productos')

	def __unicode__(self):
	    return self.nombre

	@models.permalink
	def get_absolute_url(self):
		return ('producto', (), { 'producto_slug': self.slug })

	def get_price(self):
	    return self.precio_unitario

	def get_peso_total(self):
	    return self.peso*self.stock

	def get_name(self):
	    return self.nombre