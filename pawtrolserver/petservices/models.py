from django.contrib.gis.db import models
from django.core.exceptions import ValidationError

from pets.models import Pet
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
    ENERGY_LEVEL = 'energy-level'
    SOCIAL_RATING = 'social-rating'
    OBEDIENCE_RATING = 'obedience-rating'
    MOOD = 'mood'

    RATING_CHOICES = (
        (ENERGY_LEVEL, ENERGY_LEVEL),
        (SOCIAL_RATING, SOCIAL_RATING),
        (OBEDIENCE_RATING, OBEDIENCE_RATING),
        (MOOD, MOOD),
    )

    NOTIFICATION_TYPE_CHOICES = (
        (PEE, PEE),
        (POOP, POOP),
        (ALERT, ALERT),
    )

    notification_type = models.CharField(max_length=100, choices=NOTIFICATION_TYPE_CHOICES + RATING_CHOICES)
    time = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=2, decimal_places=2, null=True)
    note = models.TextField(blank=True)

    pet_walk = models.ForeignKey('PetWalk')

    def clean(self):
        super(OnWalkNote, self).clean()
        if self.notification_type in OnWalkNote.RATING_CHOICES and self.rating is None:
            raise ValidationError({'rating': 'Value of type of notification should be have the rating set'})
        elif self.notification_type==ALERT and self.note is None:
            raise ValidationError({'note': 'Value of type of notification should be have a note populated'})
