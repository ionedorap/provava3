# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acesso',
            name='saida',
            field=models.DateTimeField(verbose_name=b'Sa\xc3\xadda'),
        ),
    ]
