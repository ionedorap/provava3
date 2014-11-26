# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_auto_20141124_2203'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='acesso',
            unique_together=set([('usuario', 'local', 'entrada')]),
        ),
    ]
