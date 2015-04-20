# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20150419_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=django_extensions.db.fields.ShortUUIDField(blank=True, unique=True, editable=False, error_messages={b'unique': 'A user with that slug already exists.'}),
        ),
    ]
