# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20141124_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='acesso',
            name='usuario',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Usu\xc3\xa1rio'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='acesso',
            name='entrada',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
