# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personalrecords', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_record',
            name='checha',
            field=models.DateField(null=True),
        ),
    ]
