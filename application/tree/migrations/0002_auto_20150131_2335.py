# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_number', models.CharField(max_length=500, null=True, blank=True)),
                ('street_name', models.CharField(max_length=500, null=True, blank=True)),
                ('neighbourhood', models.CharField(max_length=500, null=True, blank=True)),
                ('apartment_number', models.CharField(max_length=500, null=True, blank=True)),
                ('house_type', models.CharField(max_length=500, null=True, blank=True)),
                ('city', models.ForeignKey(blank=True, to='tree.City', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='livinglocation',
            name='address',
            field=models.ForeignKey(blank=True, to='tree.House', null=True),
            preserve_default=True,
        ),
    ]
