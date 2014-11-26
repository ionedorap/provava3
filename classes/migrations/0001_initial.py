# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='acesso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('entrada', models.DateTimeField(auto_now=True, verbose_name=b'Entrada')),
                ('saida', models.DateTimeField(auto_now=True, verbose_name=b'Sa\xc3\xadda')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='local',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('area', models.CharField(max_length=100, null=True, verbose_name=b'area')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('area', models.CharField(max_length=100, null=True, verbose_name=b'area de atua\xc3\xa7\xc3\xa3o')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='acesso',
            name='local',
            field=models.ForeignKey(verbose_name=b'Local', to='classes.local', null=True),
            preserve_default=True,
        ),
    ]
