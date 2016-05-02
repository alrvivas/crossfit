# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20160226_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='devolucion',
            field=models.BooleanField(default=False, verbose_name=b'Acepta devolucion'),
        ),
    ]
