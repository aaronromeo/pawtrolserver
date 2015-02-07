# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnWalkNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notification_type', models.CharField(max_length=15, choices=[(b'pee', b'pee'), (b'poop', b'poop'), (b'poop', b'poop')])),
                ('time', models.DateTimeField(auto_now_add=True)),
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
                ('walked_by', models.ForeignKey(to='profiles.WalkerProfile')),
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
                ('feedback_by', models.ForeignKey(to='profiles.OwnerProfile')),
                ('pack_walk', models.ForeignKey(to='petservices.PackWalk')),
                ('pet', models.ForeignKey(to='common.Pet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pet_walk', models.ForeignKey(to='petservices.PetWalk')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='onwalknote',
            name='pet_walk',
            field=models.ForeignKey(to='petservices.PetWalk'),
            preserve_default=True,
        ),
    ]
