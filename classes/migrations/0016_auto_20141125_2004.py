# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0015_auto_20141125_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='advertencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entrada', models.DateTimeField(auto_now=True)),
                ('local', models.ForeignKey(verbose_name=b'Local', to='classes.local', null=True)),
                ('usuario', models.ForeignKey(verbose_name=b'usuario', to='classes.usuario', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='acesso',
            name='usuario',
            field=models.ForeignKey(verbose_name=b'usuario', to='classes.usuario', null=True),
        ),
        migrations.AlterField(
            model_name='local',
            name='nivel',
            field=models.IntegerField(max_length=1, null=True, verbose_name=b'N\xc3\xadvel de Acesso', choices=[(b'1', b'livre'), (b'2', b'reservado'), (b'3', b'restrito')]),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nivel',
            field=models.IntegerField(max_length=1, null=True, verbose_name=b'N\xc3\xadvel de Acesso', choices=[(b'1', b'livre'), (b'2', b'reservado'), (b'3', b'restrito')]),
        ),
    ]
