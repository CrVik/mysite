# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20151129_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='testDate',
            field=models.DateField(verbose_name='qweqweqwe', default=datetime.datetime(2015, 11, 29, 18, 48, 3, 44787, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
