# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_auto_20160502_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='devolucion_producto',
            name='asignada',
            field=models.BooleanField(default=False, verbose_name=b'Devoluci\xc3\xb3n Asignada'),
        ),
    ]
