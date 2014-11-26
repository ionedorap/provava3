# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_auto_20141124_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acesso',
            name='saida',
            field=models.DateTimeField(null=True, verbose_name=b'Sa\xc3\xadda', blank=True),
        ),
    ]
