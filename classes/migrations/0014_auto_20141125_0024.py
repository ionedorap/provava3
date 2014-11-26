# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0013_auto_20141124_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='area',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Area'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='area',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Area de atua\xc3\xa7\xc3\xa3o'),
        ),
        migrations.AlterUniqueTogether(
            name='acesso',
            unique_together=set([('usuario', 'local', 'saida')]),
        ),
    ]
