# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '__first__'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownerprofile',
            name='badges',
            field=models.ManyToManyField(to='feedback.Badge'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='walkerprofile',
            name='badges',
            field=models.ManyToManyField(to='feedback.Badge'),
            preserve_default=True,
        ),
    ]
