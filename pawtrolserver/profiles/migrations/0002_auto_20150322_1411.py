# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walkerprofile',
            name='subscription_status',
            field=models.CharField(default=b'trial', max_length=10, choices=[(b'trial', b'trial'), (b'active', b'active'), (b'delinquent', b'delinquent'), (b'suspended', b'suspended'), (b'unsubscribed', b'unsubscribed')]),
            preserve_default=True,
        ),
    ]
