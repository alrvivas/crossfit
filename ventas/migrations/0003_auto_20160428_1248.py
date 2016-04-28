# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_auto_20160414_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abono',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=140)),
                ('cantidad', models.DecimalField(null=True, max_digits=10, decimal_places=3, blank=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fehca_modificacion', models.DateTimeField(auto_now=True, verbose_name=b'Ultima Modificacion')),
            ],
        ),
        migrations.RemoveField(
            model_name='orden',
            name='tipo_abono',
        ),
        migrations.DeleteModel(
            name='Tipo_Abono',
        ),
        migrations.AddField(
            model_name='abono',
            name='orden',
            field=models.ForeignKey(verbose_name=b'Orden Producto', blank=True, to='ventas.Orden', null=True),
        ),
    ]
