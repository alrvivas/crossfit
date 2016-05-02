# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_sku'),
        ('ventas', '0004_auto_20160428_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devoluvcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fehca_modificacion', models.DateTimeField(auto_now=True, verbose_name=b'Ultima Modificacion')),
                ('subtotal', models.DecimalField(null=True, max_digits=10, decimal_places=4)),
                ('total', models.DecimalField(null=True, max_digits=10, decimal_places=4)),
                ('total_peso', models.DecimalField(null=True, max_digits=10, decimal_places=4)),
                ('observacion', models.TextField(null=True, blank=True)),
                ('orden', models.ForeignKey(verbose_name=b'Orden', blank=True, to='ventas.Orden', null=True)),
            ],
            options={
                'verbose_name': 'Devolucion',
                'verbose_name_plural': 'Devoluciones',
            },
        ),
        migrations.CreateModel(
            name='Devoluvcion_Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)),
                ('cantidad', models.IntegerField(null=True, blank=True)),
                ('subtotal_producto', models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)),
                ('subtotal_peso', models.DecimalField(null=True, max_digits=30, decimal_places=3, blank=True)),
                ('devoluvcion', models.ForeignKey(verbose_name=b'Orden Producto', blank=True, to='ventas.Devoluvcion', null=True)),
                ('producto', models.ForeignKey(blank=True, to='productos.Producto', null=True)),
            ],
        ),
    ]
