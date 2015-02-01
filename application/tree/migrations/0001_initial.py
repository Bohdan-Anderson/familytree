# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BirthLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hospital', models.CharField(max_length=500, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=500, null=True, blank=True)),
                ('prov_state', models.CharField(max_length=500, null=True, blank=True)),
                ('country', models.CharField(max_length=500, null=True, blank=True)),
                ('lon', models.FloatField(default=0, null=True, blank=True)),
                ('lat', models.FloatField(default=0, null=True, blank=True)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FamilyName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500, null=True, blank=True)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=500, null=True, blank=True)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Livinglocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('moved_to', models.DateField(null=True, blank=True)),
                ('moved_from', models.DateField(null=True, blank=True)),
                ('city', models.ForeignKey(blank=True, to='tree.City', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brith', models.DateField()),
                ('death', models.DateField(null=True, blank=True)),
                ('sex', models.CharField(default=b'm', max_length=1, choices=[(b'm', b'male'), (b'f', b'female')])),
                ('name_given', models.CharField(max_length=500, null=True, blank=True)),
                ('name_middle', models.CharField(max_length=500, null=True, blank=True)),
                ('slug', models.SlugField(blank=True)),
                ('birth_location', models.ForeignKey(blank=True, to='tree.BirthLocation', null=True)),
                ('death_city', models.ForeignKey(blank=True, to='tree.City', null=True)),
                ('living_in', models.ManyToManyField(to='tree.Livinglocation', null=True, blank=True)),
                ('name_family', models.ForeignKey(blank=True, to='tree.FamilyName', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to=b'work-img', blank=True)),
                ('taken', models.DateField(null=True, blank=True)),
                ('location', models.ManyToManyField(to='tree.City', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relation', models.CharField(default=b'm', max_length=2, choices=[(b'm', b'Mother'), (b'f', b'Father'), (b'sm', b'StepMother'), (b'sf', b'StepFather'), (b'gm', b'God Mother'), (b'gf', b'God Farther')])),
                ('adopted', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagPerson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_x', models.FloatField(default=0, null=True, blank=True)),
                ('location_y', models.FloatField(default=0, null=True, blank=True)),
                ('person', models.ManyToManyField(to='tree.Person', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='picture',
            name='tag_person',
            field=models.ManyToManyField(to='tree.TagPerson', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='parents',
            field=models.ManyToManyField(to='tree.Relations', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='includes',
            field=models.ManyToManyField(to='tree.Person', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='locations',
            field=models.ManyToManyField(to='tree.City', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='picture',
            field=models.ManyToManyField(to='tree.Picture', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='birthlocation',
            name='city',
            field=models.ForeignKey(blank=True, to='tree.City', null=True),
            preserve_default=True,
        ),
    ]
