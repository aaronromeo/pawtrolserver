from django.contrib.gis.db import models

from common.models import Pet
from profiles.models import WalkerProfile, OwnerProfile


class PackWalk(models.Model):
    '''
    Model to allow a walker to assoicate multiple pet walks.
    e.g. Taking a group of dogs out for a walk or to the dog park.

    This can also only have one associate pet walk.

    '''
    description = models.CharField(max_length=255)

    walked_by = models.ForeignKey(WalkerProfile)


class PetWalk(models.Model):
    '''
    Model used to track walk specific information for a single pet, in addition to the association between a pet,
    an owner's feedback and the walker (via the PackWalk)
    '''

    UNHAPPY = 'unhappy'
    SATISFIED = 'satisfied'
    HAPPY = 'happy'

    SATISFACTION_CHOICES = (
        (UNHAPPY, UNHAPPY),
        (SATISFIED, SATISFIED),
        (HAPPY, HAPPY),
    )

    pet = models.ForeignKey(Pet)
    pack_walk = models.ForeignKey('PackWalk')

    satisfaction = models.CharField(max_length=15, choices=SATISFACTION_CHOICES)
    owners_notes = models.TextField(blank=True)

    walkers_notes = models.TextField(blank=True)

    pickup_lon = models.FloatField()
    pickup_lat = models.FloatField()
    end_lon = models.FloatField()
    end_lat = models.FloatField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    feedback_by = models.ForeignKey(OwnerProfile)


# class Route(models.Model):
#     '''
#     TODO: Complete this model.

#     Model to track the route of the pet walk. This might not be required.

#     '''
#     pet_walk = models.ForeignKey('PetWalk')


class OnWalkNote(models.Model):
    '''
    Tracking for notifications which happen during a walk

    '''

    PEE = 'pee'
    POOP = 'poop'
    ALERT = 'alert'

    NOTIFICATION_TYPE_CHOICES = (
        (PEE, PEE),
        (POOP, POOP),
        (POOP, POOP),
    )

    notification_type = models.CharField(max_length=15, choices=NOTIFICATION_TYPE_CHOICES)
    time = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)

    pet_walk = models.ForeignKey('PetWalk')
