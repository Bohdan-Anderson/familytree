# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0006_education_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cemetary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_number', models.CharField(max_length=500, null=True, blank=True)),
                ('street_name', models.CharField(max_length=500, null=True, blank=True)),
                ('city', models.ForeignKey(blank=True, to='tree.City', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, null=True, blank=True)),
                ('established', models.CharField(max_length=500, null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parnerships',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relation', models.CharField(default=b'm', max_length=2, choices=[(b'm', b'Married'), (b'd', b'Divorced')])),
                ('date', models.DateField(null=True, blank=True)),
                ('date_confirmed', models.BooleanField(default=False)),
                ('date_end', models.DateField(null=True, blank=True)),
                ('date_end_confirmed', models.BooleanField(default=False)),
                ('address', models.ForeignKey(blank=True, to='tree.House', null=True)),
                ('attended_by', models.ManyToManyField(related_name='attendedby', null=True, to='tree.Person', blank=True)),
                ('locations', models.ManyToManyField(to='tree.City', null=True, blank=True)),
                ('photos', models.ManyToManyField(to='tree.Picture', null=True, blank=True)),
                ('relation_a', models.ForeignKey(related_name='person_a', to='tree.Person')),
                ('relation_b', models.ForeignKey(related_name='person_b', to='tree.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateField(null=True, blank=True)),
                ('start_confirmed', models.BooleanField(default=False)),
                ('end', models.DateField(null=True, blank=True)),
                ('end_confirmed', models.BooleanField(default=False)),
                ('job_title', models.CharField(max_length=500, null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('at', models.ForeignKey(blank=True, to='tree.Company', null=True)),
                ('person', models.ForeignKey(to='tree.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='person',
            name='education',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='tag_person',
        ),
        migrations.AddField(
            model_name='city',
            name='changed_name_to',
            field=models.ForeignKey(related_name='changednameto', blank=True, to='tree.City', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='local_language_city',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='local_language_country',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='city',
            name='local_language_prov',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='endDate_confirmed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='notes',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='person',
            field=models.ForeignKey(related_name='related_person_education', blank=True, to='tree.Person', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='education',
            name='startDate_confirmed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.ForeignKey(blank=True, to='tree.House', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='date_confirmed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='familyname',
            name='name_native',
            field=models.ForeignKey(blank=True, to='tree.FamilyName', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='house',
            name='lat',
            field=models.FloatField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='house',
            name='lon',
            field=models.FloatField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='livinglocation',
            name='moved_from_confirmed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='livinglocation',
            name='moved_to_confirmed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='brith_confirmed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='burial_type',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='cemetary',
            field=models.ManyToManyField(to='tree.Cemetary', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='death_confirmed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='name_birth_family',
            field=models.ForeignKey(related_name='birthfamilyname', blank=True, to='tree.FamilyName', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='name_given_birth',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='name_nickname_1',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='name_nickname_2',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='plot',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='plot_lat',
            field=models.FloatField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='plot_lon',
            field=models.FloatField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='address',
            field=models.ForeignKey(blank=True, to='tree.House', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='taken_confirmed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tagperson',
            name='picture',
            field=models.ForeignKey(blank=True, to='tree.Picture', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='birth_location',
            field=models.ForeignKey(null=True, blank=True, to='tree.BirthLocation', unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='brith',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
