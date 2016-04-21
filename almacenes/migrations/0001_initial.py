# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de Creacion')),
                ('fehca_modificacion', models.DateTimeField(auto_now=True, verbose_name=b'Ultima Modificacion')),
                ('nombre', models.CharField(max_length=140, null=True)),
                ('celular', models.CharField(max_length=15, null=True)),
                ('telefono', models.CharField(max_length=15, null=True)),
            ],
        ),
    ]
