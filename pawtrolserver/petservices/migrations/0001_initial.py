# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnWalkNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notification_type', models.CharField(max_length=100, choices=[(b'pee', b'pee'), (b'poop', b'poop'), (b'alert', b'alert'), (b'energy-level', b'energy-level'), (b'social-rating', b'social-rating'), (b'obedience-rating', b'obedience-rating'), (b'mood', b'mood')])),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('rating', models.DecimalField(null=True, max_digits=2, decimal_places=2)),
                ('note', models.TextField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PackWalk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PetWalk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('satisfaction', models.CharField(max_length=15, choices=[(b'unhappy', b'unhappy'), (b'satisfied', b'satisfied'), (b'happy', b'happy')])),
                ('owners_notes', models.TextField(blank=True)),
                ('walkers_notes', models.TextField(blank=True)),
                ('pickup_lon', models.FloatField()),
                ('pickup_lat', models.FloatField()),
                ('end_lon', models.FloatField()),
                ('end_lat', models.FloatField()),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
