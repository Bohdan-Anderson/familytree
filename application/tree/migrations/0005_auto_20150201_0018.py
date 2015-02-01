# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0004_auto_20150131_2353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startDate', models.DateField(null=True, blank=True)),
                ('endDate', models.DateField(null=True, blank=True)),
                ('education_level', models.CharField(max_length=500, null=True, blank=True)),
                ('subject', models.CharField(max_length=500, null=True, blank=True)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_name', models.CharField(max_length=500, null=True, blank=True)),
                ('city', models.ForeignKey(blank=True, to='tree.City', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='education',
            field=models.ManyToManyField(to='tree.Education', null=True, blank=True),
            preserve_default=True,
        ),
    ]
