from datetime import datetime
from random import randint

from django.core.management.base import BaseCommand, CommandError
from profiles.models import *
from profiles.serializers import *


class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def datestamp(self):
        now = datetime.now()
        datestamp = "{}{}{}{}{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
        return datestamp

    def test_serializer(self, serializer):
        if not serializer.is_valid():
            raise CommandError('Serializer not valid: {}'.format(serializer.errors))

    def setupWalker(self, fname):
        datestamp = self.datestamp()
        data = {
            'email': 'walker+{}@pawtrolapp.com'.format(datestamp), 
            'first_name': fname, 
            'last_name': 'Walker-{}'.format(datestamp), 
            'password': 'password123', 
            'phone_number': '{}'.format(randint(1000000000, 99999999999)), 
            'address': '123123'
        }
        userserializer = UserSerializer(data=data)
        self.test_serializer(userserializer)
        user = userserializer.save()
        walkerserializer = WalkerProfileSerializer(data={'user': user.pk})
        self.test_serializer(walkerserializer)
        walkerprofile = walkerserializer.save()

        return walkerprofile

    def setupOwner(self, fname):
        datestamp = self.datestamp()
        data = {
            'email': 'owner+{}@pawtrolapp.com'.format(datestamp), 
            'first_name': fname, 
            'last_name': 'Owner-{}'.format(datestamp), 
            'password': 'password123', 
            'phone_number': '{}'.format(randint(1000000000, 99999999999)), 
            'address': '123123'
        }
        userserializer = UserSerializer(data=data)
        self.test_serializer(userserializer)
        user = userserializer.save()
        ownerserializer = OwnerProfileSerializer(data={'user': user.pk})
        self.test_serializer(ownerserializer)
        ownerprofile = ownerserializer.save()

        return ownerprofile

    def _populate(self):
        self.setupWalker('Fred')
        self.setupWalker('Bill')

        self.setupOwner('Ben')
        self.setupOwner('Jake')
        self.setupOwner('Jen')

    def handle(self, *args, **options):
        self._populate()
