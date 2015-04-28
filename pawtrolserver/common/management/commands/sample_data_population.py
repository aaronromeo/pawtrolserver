from datetime import datetime
from random import randint

from django.core.management.base import BaseCommand, CommandError

from profiles.models import *
from profiles.serializers import *
from petservices.models import *
from petservices.serializers import *


# TODO: Instqll FactoryBoy and use that.


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

    def setupBusness(self, business_name, walker):
        datestamp = self.datestamp()
        data = {
            'business_name': '{}+{}'.format(business_name, datestamp),
            'business_owner': walker.user.username,
        }
        businessserializer = ServiceBusinessSerializer(data=data)
        self.test_serializer(businessserializer)
        business = businessserializer.save()

        walkerserializer = WalkerProfileSerializer(walker, data={'businesses': [business.uuid, ]}, partial=True)
        self.test_serializer(walkerserializer)
        walkerserializer.save()

        return business

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
        walkerserializer = WalkerProfileSerializer(
            data={
                'user': user.username
            }
        )
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
        ownerserializer = OwnerProfileSerializer(
            data={
                'user': user.username,
            }
        )
        self.test_serializer(ownerserializer)
        ownerprofile = ownerserializer.save()

        return ownerprofile

    def setupDog(self, name, owner):
        datestamp = self.datestamp()

        breed_list = ['French Bulldog', 'Boston Terrier', 'Labrador Retriever', 'Poodle', 'Doberman Pincer', 'German Shepard']
        color_list = [color[0] for color in Dog.COLOR_CHOICES]

        data = {
            'name': name,
            'ownerprofile': owner.user.username,
            'primary_breed': breed_list[randint(0, len(breed_list)-1)],
            'primary_coat_color': color_list[randint(0, len(color_list)-1)],
        }
        dogserializer = DogSerializer(data=data)
        self.test_serializer(dogserializer)
        dog = dogserializer.save()

        return dog

    def _populate(self):
        User.objects.create_superuser(username='aaron', email='aaron@pawtrol.com', password='password123')

        fred = self.setupWalker('Fred')
        self.setupBusness('Fred likes to walk', fred)

        bill = self.setupWalker('Bill')
        self.setupBusness('Bill digs your dogs', bill)

        ben = self.setupOwner('Ben')
        jake = self.setupOwner('Jake')
        jen = self.setupOwner('Jen')

        self.setupDog('Charlie', ben)
        self.setupDog('Spot', ben)
        self.setupDog('Goldie', jake)
        self.setupDog('Whiskey', jen)
        self.setupDog('Digby', jen)

    def handle(self, *args, **options):
        self._populate()
