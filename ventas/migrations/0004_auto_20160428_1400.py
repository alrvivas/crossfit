# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_auto_20160428_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abono',
            name='nombre',
        ),
        migrations.AlterField(
            model_name='abono',
            name='orden',
            field=models.ForeignKey(verbose_name=b'Orden', blank=True, to='ventas.Orden', null=True),
        ),
    ]
