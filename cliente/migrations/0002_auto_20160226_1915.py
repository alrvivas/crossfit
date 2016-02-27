# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='imagen',
            field=models.ImageField(default=b'images/clientes/default-01.jpg', upload_to=b'images/clientes', null=True, verbose_name=b'Imagen Cliente', blank=True),
        ),
    ]
