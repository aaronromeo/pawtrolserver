# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('petservices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dog',
            name='dob',
            field=models.DateField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dog',
            name='microchip_number',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dog',
            name='primary_breed',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dog',
            name='weight',
            field=models.DecimalField(null=True, max_digits=4, decimal_places=1),
            preserve_default=True,
        ),
    ]
