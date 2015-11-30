# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20151129_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='quiestion',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='quiestion_text',
            new_name='question_text',
        ),
    ]
