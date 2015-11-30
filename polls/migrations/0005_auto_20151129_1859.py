# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20151129_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='testDate',
            new_name='create_date',
        ),
    ]
