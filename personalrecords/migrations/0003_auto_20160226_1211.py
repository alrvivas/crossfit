# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personalrecords', '0002_personal_record_checha'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal_record',
            old_name='checha',
            new_name='fhecha',
        ),
    ]
