# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0005_auto_20150201_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='school',
            field=models.ForeignKey(blank=True, to='tree.School', null=True),
            preserve_default=True,
        ),
    ]
