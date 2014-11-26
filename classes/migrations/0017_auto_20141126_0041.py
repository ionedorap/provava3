# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0016_auto_20141125_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nivel',
            field=models.CharField(max_length=5, null=True, verbose_name=b'N\xc3\xadvel de Acesso', choices=[(b'1', b'livre'), (b'2', b'reservado'), (b'3', b'restrito')]),
        ),
    ]
