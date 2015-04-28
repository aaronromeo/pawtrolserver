# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20150419_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceBusiness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', django_extensions.db.fields.ShortUUIDField(blank=True, unique=True, editable=False, error_messages={b'unique': 'A business with that UUID already exists.'})),
                ('business_name', models.CharField(max_length=200, verbose_name='business name')),
                ('subscription_status', models.CharField(default=b'trial', max_length=10, choices=[(b'trial', b'trial'), (b'active', b'active'), (b'delinquent', b'delinquent'), (b'suspended', b'suspended'), (b'unsubscribed', b'unsubscribed')])),
                ('subscription_expiration_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date subscription expires')),
                ('business_owner', models.ForeignKey(help_text='Setup so that a business can be assoiciated to any user regardless of whether they have a business profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='walkerprofile',
            name='subscription_expiration_date',
        ),
        migrations.RemoveField(
            model_name='walkerprofile',
            name='subscription_status',
        ),
        migrations.AddField(
            model_name='walkerprofile',
            name='businesses',
            field=models.ManyToManyField(to='profiles.ServiceBusiness'),
        ),
    ]
