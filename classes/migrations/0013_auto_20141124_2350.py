# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0012_auto_20141124_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='nivel',
            field=models.CharField(max_length=1, null=True, verbose_name=b'N\xc3\xadvel de Acesso', choices=[(b'1', b'livre'), (b'2', b'reservado'), (b'3', b'restrito')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usuario',
            name='nivel',
            field=models.CharField(max_length=1, null=True, verbose_name=b'N\xc3\xadvel de Acesso', choices=[(b'1', b'livre'), (b'2', b'reservado'), (b'3', b'restrito')]),
            preserve_default=True,
        ),
    ]
