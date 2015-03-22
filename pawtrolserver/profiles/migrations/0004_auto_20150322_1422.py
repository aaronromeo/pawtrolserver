# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20150322_1420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='walkerprofile',
            old_name='default_rate_per_walk_hour',
            new_name='default_rate_per_hour_walked',
        ),
    ]
