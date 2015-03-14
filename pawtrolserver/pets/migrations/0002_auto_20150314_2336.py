# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='owner',
            field=models.ForeignKey(to='profiles.OwnerProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pack',
            name='leader_profile',
            field=models.ForeignKey(to='profiles.WalkerProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pack',
            name='pets',
            field=models.ManyToManyField(to='pets.Pet'),
            preserve_default=True,
        ),
    ]
