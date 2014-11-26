# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0008_auto_20141124_2217'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='acesso',
            unique_together=set([('usuario', 'local')]),
        ),
    ]
