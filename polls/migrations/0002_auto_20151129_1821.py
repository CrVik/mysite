# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(verbose_name='Ответ на вопрос', max_length=200),
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(verbose_name='Количесвто ответов', default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiestion_text',
            field=models.CharField(verbose_name='Текс вопроса', max_length=200),
        ),
    ]
