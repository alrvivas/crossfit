# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejercicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benchmark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('tiempo', models.PositiveIntegerField(null=True)),
                ('tiempo_pr', models.PositiveIntegerField(null=True)),
                ('repeticiones_pr', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ejercicio_Benchmark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('repeticiones', models.PositiveIntegerField(null=True)),
                ('benchmark', models.ForeignKey(to='benchmarks.Benchmark', null=True)),
                ('ejercicio', models.ForeignKey(to='ejercicios.Ejercicio', null=True)),
            ],
        ),
    ]
