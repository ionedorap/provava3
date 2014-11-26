# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0014_auto_20141125_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acesso',
            name='saida',
            field=models.TimeField(null=True, verbose_name=b'Saida', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='acesso',
            unique_together=None,
        ),
    ]
