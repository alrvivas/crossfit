# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140, verbose_name=b'Nombre Categoria')),
                ('slug', models.SlugField(null=True, blank=True, help_text=b'Valor unico por producto URL pagina, creado desde nombre.', unique=True)),
                ('activo', models.BooleanField(default=True)),
                ('orden', models.PositiveIntegerField(null=True, blank=True)),
                ('imagen', models.ImageField(default=b'images/producto/categorias/default-01.png', upload_to=b'images/producto/categorias', null=True, verbose_name=b'Imagen Categoria', blank=True)),
            ],
            options={
                'ordering': ['orden'],
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255, verbose_name=b'Nombre')),
                ('slug', models.SlugField(null=True, blank=True, unique=True, verbose_name=b'Slug')),
                ('activo', models.BooleanField(default=False, verbose_name=b'Activo')),
                ('codigo_barras', models.CharField(max_length=20, unique=True, null=True, blank=True)),
                ('vida_anaquel', models.IntegerField(blank=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de Creacion')),
                ('fehca_modificacion', models.DateTimeField(auto_now=True, verbose_name=b'Ultima Modificacion')),
                ('orden', models.PositiveIntegerField()),
                ('stock', models.IntegerField(null=True, blank=True)),
                ('precio_unitario', models.DecimalField(verbose_name=b'Precio', max_digits=30, decimal_places=3)),
                ('presentacion', models.CharField(max_length=50, null=True, blank=True)),
                ('unidad', models.IntegerField(default=1, blank=True)),
                ('peso', models.DecimalField(max_digits=30, decimal_places=3)),
                ('imagen', models.ImageField(default=b'images/producto/default-01.png', upload_to=b'images/producto', null=True, verbose_name=b'Imagen Categoria', blank=True)),
                ('categoria', models.ForeignKey(to='productos.Categoria')),
            ],
            options={
                'ordering': ['categoria', 'orden'],
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
