# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0007_devolucion_producto_asignada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devolucion_producto',
            name='asignada',
        ),
        migrations.AddField(
            model_name='devolucion',
            name='asignada',
            field=models.BooleanField(default=False, verbose_name=b'Devoluci\xc3\xb3n Asignada'),
        ),
    ]
