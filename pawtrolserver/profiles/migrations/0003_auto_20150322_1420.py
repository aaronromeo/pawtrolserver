# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20150322_1411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='walkerprofile',
            name='default_rate_per_walk',
        ),
        migrations.AddField(
            model_name='walkerprofile',
            name='default_rate_per_walk_hour',
            field=models.DecimalField(default=20, max_digits=4, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='walkerprofile',
            name='subscription_expiration_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date subscription expires'),
            preserve_default=True,
        ),
    ]
