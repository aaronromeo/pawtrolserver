# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20150314_2336'),
        ('profiles', '0001_initial'),
        ('petservices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='petwalk',
            name='feedback_by',
            field=models.ForeignKey(to='profiles.OwnerProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='petwalk',
            name='pack_walk',
            field=models.ForeignKey(to='petservices.PackWalk'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='petwalk',
            name='pet',
            field=models.ForeignKey(to='pets.Pet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='packwalk',
            name='walked_by',
            field=models.ForeignKey(to='profiles.WalkerProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='onwalknote',
            name='pet_walk',
            field=models.ForeignKey(to='petservices.PetWalk'),
            preserve_default=True,
        ),
    ]
