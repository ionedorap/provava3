# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_auto_20141124_2146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acesso',
            name='nome',
        ),
        migrations.AlterField(
            model_name='acesso',
            name='usuario',
            field=models.ForeignKey(verbose_name=b'usu\xc3\xa1rio', to='classes.usuario', null=True),
        ),
    ]
