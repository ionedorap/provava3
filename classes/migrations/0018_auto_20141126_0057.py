# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0017_auto_20141126_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='nivel',
            field=models.IntegerField(max_length=5, null=True, verbose_name=b'N\xc3\xadvel de Acesso', choices=[(b'1', b'livre'), (b'2', b'reservado'), (b'3', b'restrito')]),
        ),
    ]
