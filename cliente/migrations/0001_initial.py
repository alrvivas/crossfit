# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_registro', models.DateField(null=True)),
                ('nombre', models.CharField(max_length=140, null=True)),
                ('apellidos', models.CharField(max_length=140, null=True)),
                ('celular', models.CharField(max_length=15, null=True)),
                ('telefono', models.CharField(max_length=15, null=True)),
                ('dias_credito', models.PositiveIntegerField(null=True)),
                ('imagen', models.ImageField(default=b'images/clientes/default-01.png', upload_to=b'images/clientes', null=True, verbose_name=b'Imagen Cliente', blank=True)),
            ],
        ),
    ]
