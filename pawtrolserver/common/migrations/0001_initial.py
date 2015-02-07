# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('leader_profile', models.ForeignKey(to='profiles.WalkerProfile')),
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
                ('owner', models.ForeignKey(to='profiles.OwnerProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pack',
            name='pets',
            field=models.ManyToManyField(to='common.Pet'),
            preserve_default=True,
        ),
    ]
