# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.TextField(blank=True)),
                ('phone_number', models.CharField(max_length=11, blank=True)),
                ('avatar', models.ImageField(upload_to=b'', blank=True)),
                ('date_last_seen', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WalkerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.TextField(blank=True)),
                ('phone_number', models.CharField(max_length=11, blank=True)),
                ('avatar', models.ImageField(upload_to=b'', blank=True)),
                ('date_last_seen', models.DateTimeField(auto_now_add=True)),
                ('subscription_status', models.CharField(max_length=10, choices=[(b'trial', b'trial'), (b'active', b'active'), (b'delinquent', b'delinquent'), (b'suspended', b'suspended'), (b'unsubscribed', b'unsubscribed')])),
                ('subscription_expiration_date', models.DateTimeField()),
                ('default_rate_per_walk', models.DecimalField(max_digits=4, decimal_places=1)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ownerprofile',
            name='preferred_walkers',
            field=models.ManyToManyField(to='profiles.WalkerProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ownerprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
