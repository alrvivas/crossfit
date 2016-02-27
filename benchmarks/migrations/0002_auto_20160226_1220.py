# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('benchmarks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benchmark',
            name='tiempo',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='benchmark',
            name='tiempo_pr',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
