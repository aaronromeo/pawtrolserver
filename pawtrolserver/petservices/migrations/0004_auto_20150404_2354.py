# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petservices', '0003_auto_20150404_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='coat_pattern',
            field=models.CharField(blank=True, max_length=10, choices=[(b'x_and_tan', b'black and tan/liver and tan/blue and tan'), (b'bicolor', b'bicolor'), (b'tricolor', b'tricolor'), (b'merle', b'merle'), (b'tuxedo', b'tuxedo'), (b'harlequin', b'harlequin'), (b'speckled', b'speckled/belton'), (b'brindle', b'brindle'), (b'saddle', b'saddle/blanket'), (b'sable', b'sable')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dog',
            name='primary_coat_color',
            field=models.CharField(blank=True, max_length=10, choices=[(b'brown', b'brown'), (b'red', b'red'), (b'gold', b'gold'), (b'yellow', b'yellow'), (b'cream', b'cream'), (b'black', b'black'), (b'blue', b'blue'), (b'grey', b'grey'), (b'white', b'white')]),
            preserve_default=True,
        ),
    ]
