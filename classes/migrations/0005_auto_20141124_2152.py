# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20141124_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entrada', models.DateTimeField(auto_now=True)),
                ('local', models.ForeignKey(verbose_name=b'Local', to='classes.local', null=True)),
                ('usuario', models.ForeignKey(verbose_name=b'usu\xc3\xa1rio', to='classes.usuario', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='saida',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('saida', models.DateTimeField(verbose_name=b'Sa\xc3\xadda')),
                ('local', models.ForeignKey(verbose_name=b'Local', to='classes.local', null=True)),
                ('usuario', models.ForeignKey(verbose_name=b'usu\xc3\xa1rio', to='classes.usuario', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='acesso',
            name='local',
        ),
        migrations.RemoveField(
            model_name='acesso',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='acesso',
        ),
    ]
