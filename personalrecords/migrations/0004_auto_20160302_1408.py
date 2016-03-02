# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personalrecords', '0003_auto_20160226_1211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal_record',
            old_name='fhecha',
            new_name='fecha',
        ),
    ]
