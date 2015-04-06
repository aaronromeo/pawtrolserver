# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petservices', '0002_auto_20150404_2323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dog',
            old_name='owner',
            new_name='ownerprofile',
        ),
    ]
