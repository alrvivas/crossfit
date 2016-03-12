# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20160226_1915'),
        ('productos', '0002_producto_sku'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estatus_Cobranza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estatus_Orden',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fehca_modificacion', models.DateTimeField(auto_now=True, verbose_name=b'Ultima Modificacion')),
                ('comision_leche', models.DecimalField(null=True, max_digits=10, decimal_places=4)),
                ('subtotal', models.DecimalField(null=True, max_digits=10, decimal_places=4)),
                ('total', models.DecimalField(null=True, max_digits=10, decimal_places=4)),
                ('total_peso', models.DecimalField(null=True, max_digits=10, decimal_places=4)),
                ('saldo', models.DecimalField(null=True, max_digits=10, decimal_places=4)),
                ('observacion', models.TextField(null=True, blank=True)),
                ('cliente', models.ForeignKey(blank=True, to='cliente.Cliente', null=True)),
                ('estatus_cobranza', models.ForeignKey(blank=True, to='ventas.Estatus_Cobranza', null=True)),
                ('estatus_orden', models.ForeignKey(blank=True, to='ventas.Estatus_Orden', null=True)),
            ],
            options={
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Ordenes',
            },
        ),
        migrations.CreateModel(
            name='Orden_Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)),
                ('cantidad', models.IntegerField(null=True, blank=True)),
                ('subtotal', models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)),
                ('subtotal_peso', models.DecimalField(null=True, max_digits=30, decimal_places=3, blank=True)),
                ('orden', models.ForeignKey(verbose_name=b'Orden Producto', blank=True, to='ventas.Orden', null=True)),
                ('producto', models.ForeignKey(blank=True, to='productos.Producto', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Abono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
            ],
        ),
        migrations.AddField(
            model_name='orden',
            name='tipo_abono',
            field=models.ForeignKey(blank=True, to='ventas.Tipo_Abono', null=True),
        ),
        migrations.AddField(
            model_name='orden',
            name='tipo_pago',
            field=models.ForeignKey(blank=True, to='ventas.Tipo_Pago', null=True),
        ),
    ]
