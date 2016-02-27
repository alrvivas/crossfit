# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('ejercicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal_Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pr', models.CharField(max_length=20, null=True)),
                ('cliente', models.ForeignKey(to='cliente.Cliente', null=True)),
                ('ejercicio', models.ForeignKey(to='ejercicios.Ejercicio', null=True)),
            ],
        ),
    ]
