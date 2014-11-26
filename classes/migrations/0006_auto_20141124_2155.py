# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_auto_20141124_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='acesso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entrada', models.DateTimeField(auto_now=True)),
                ('saida', models.DateTimeField(null=True, verbose_name=b'Sa\xc3\xadda')),
                ('local', models.ForeignKey(verbose_name=b'Local', to='classes.local', null=True)),
                ('usuario', models.ForeignKey(verbose_name=b'usu\xc3\xa1rio', to='classes.usuario', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='entrada',
            name='local',
        ),
        migrations.RemoveField(
            model_name='entrada',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='entrada',
        ),
        migrations.RemoveField(
            model_name='saida',
            name='local',
        ),
        migrations.RemoveField(
            model_name='saida',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='saida',
        ),
    ]
