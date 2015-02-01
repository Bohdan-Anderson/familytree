# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0002_auto_20150131_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='relations',
            name='parent',
            field=models.ForeignKey(blank=True, to='tree.Person', null=True),
            preserve_default=True,
        ),
    ]
