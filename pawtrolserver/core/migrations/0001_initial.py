# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('leader', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('species', models.CharField(max_length=20, choices=[(b'dog', b'Dog'), (b'cat', b'Cat')])),
                ('dob', models.DateField()),
                ('is_dob_estimated', models.BooleanField(default=False)),
                ('primary_breed', models.CharField(max_length=255)),
                ('secondary_breed', models.CharField(max_length=255, blank=True)),
                ('primary_coat_color', models.CharField(max_length=10, choices=[(b'brown', b'brown'), (b'red', b'red'), (b'gold', b'gold'), (b'yellow', b'yellow'), (b'cream', b'cream'), (b'black', b'black'), (b'blue', b'blue'), (b'grey', b'grey'), (b'white', b'white')])),
                ('secondary_coat_color', models.CharField(blank=True, max_length=10, choices=[(b'brown', b'brown'), (b'red', b'red'), (b'gold', b'gold'), (b'yellow', b'yellow'), (b'cream', b'cream'), (b'black', b'black'), (b'blue', b'blue'), (b'grey', b'grey'), (b'white', b'white')])),
                ('coat_pattern', models.CharField(max_length=10, choices=[(b'x_and_tan', b'black and tan/liver and tan/blue and tan'), (b'bicolor', b'bicolor'), (b'tricolor', b'tricolor'), (b'merle', b'merle'), (b'tuxedo', b'tuxedo'), (b'harlequin', b'harlequin'), (b'speckled', b'speckled/belton'), (b'brindle', b'brindle'), (b'saddle', b'saddle/blanket'), (b'sable', b'sable')])),
                ('description', models.TextField(blank=True)),
                ('weight', models.DecimalField(max_digits=4, decimal_places=1)),
                ('microchip_number', models.CharField(max_length=255)),
                ('avatar', models.ImageField(upload_to=b'', blank=True)),
                ('vet_name', models.CharField(max_length=255, blank=True)),
                ('vet_number', models.CharField(max_length=11, blank=True)),
                ('date_joined', models.DateTimeField(null=True, blank=True)),
                ('owner', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.TextField(blank=True)),
                ('phone_number', models.CharField(max_length=11, blank=True)),
                ('avatar', models.ImageField(upload_to=b'', blank=True)),
                ('date_last_seen', models.DateTimeField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Walk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=255)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('pickup_lon', models.FloatField()),
                ('pickup_lat', models.FloatField()),
                ('end_lon', models.FloatField()),
                ('end_lat', models.FloatField()),
                ('walkers_notes', models.TextField(blank=True)),
                ('satisfaction', models.CharField(max_length=15, choices=[(b'unhappy', b'unhappy'), (b'satisfied', b'satisfied'), (b'happy', b'happy')])),
                ('owners_notes', models.TextField(blank=True)),
                ('feedback_by', models.ForeignKey(related_name='feedback_given', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('walked_by', models.ForeignKey(related_name='walks_given', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pack',
            name='pets',
            field=models.ManyToManyField(to='core.Pet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='badge',
            name='pets',
            field=models.ManyToManyField(to='core.Pet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='badge',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
