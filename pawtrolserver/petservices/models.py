from django.contrib.gis.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from feedback.models import Badge
from profiles.models import WalkerProfile, OwnerProfile


class Pet(models.Model):
    """
    The Pet Model

    """

    name = models.CharField(max_length=255)
    dob = models.DateField(null=True)
    is_dob_estimated = models.BooleanField(default=False)

    # TODO: These should be choices for ease of sorting
    primary_breed = models.CharField(max_length=255, blank=True)
    secondary_breed = models.CharField(max_length=255, blank=True)
    # primary_coat_color = models.CharField(max_length=10)
    # secondary_coat_color = models.CharField(max_length=10, blank=True)
    # coat_pattern = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    weight = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    microchip_number = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(blank=True)
    vet_name = models.CharField(max_length=255, blank=True)
    vet_number = models.CharField(max_length=11, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    badges = models.ManyToManyField(Badge)
    ownerprofile = models.ForeignKey(OwnerProfile)

    class Meta:
        abstract = True


class Dog(Pet):
    """
    The Dog specific Model

    """
    BROWN = 'brown'
    RED = 'red'
    GOLD = 'gold'
    YELLOW = 'yellow'
    CREAM = 'cream'
    BLACK = 'black'
    BLUE = 'blue'
    GREY = 'grey'
    WHITE = 'white'

    COLOR_CHOICES = (
        (BROWN, BROWN),
        (RED, RED),
        (GOLD, GOLD),
        (YELLOW, YELLOW),
        (CREAM, CREAM),
        (BLACK, BLACK),
        (BLUE, BLUE),
        (GREY, GREY),
        (WHITE, WHITE),
    )

    X_AND_TAN = 'x_and_tan'
    BICOLOR = 'bicolor'
    TRICOLOR = 'tricolor'
    MERLE = 'merle'
    TUXEDO = 'tuxedo'
    HARLEQUIN = 'harlequin'
    SPECKLED = 'speckled'
    BRINDLE = 'brindle'
    SADDLE = 'saddle'
    SABLE = 'sable'

    PATTERN_CHOICES = (
        (X_AND_TAN, 'black and tan/liver and tan/blue and tan'),
        (BICOLOR, BICOLOR),
        (TRICOLOR, TRICOLOR),
        (MERLE, MERLE),
        (TUXEDO, TUXEDO),
        (HARLEQUIN, HARLEQUIN),
        (SPECKLED, 'speckled/belton'),
        (BRINDLE, BRINDLE),
        (SADDLE, 'saddle/blanket'),
        (SABLE, SABLE),
    )

    primary_coat_color = models.CharField(max_length=10, choices=COLOR_CHOICES, blank=True)
    secondary_coat_color = models.CharField(max_length=10, choices=COLOR_CHOICES, blank=True)
    coat_pattern = models.CharField(max_length=10, choices=PATTERN_CHOICES, blank=True)


class WalkerPetMatch(models.Model):
    """
    A model to associate a Walker to group of Pets

    """

    name = models.CharField(max_length=255)

    leader_profile = models.ForeignKey(WalkerProfile)
    dogs = models.ManyToManyField('Dog')


class PackWalk(models.Model):
    '''
    Model to allow a walker to assoicate multiple pet walks.
    e.g. Taking a group of dogs out for a walk or to the dog park.

    This can also only have one associate pet walk.

    '''
    description = models.CharField(max_length=255)

    walked_by = models.ForeignKey(WalkerProfile)


class DogWalk(models.Model):
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

    dog = models.ForeignKey(Dog)
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

    dog_walk = models.ForeignKey('DogWalk')

    def clean(self):
        super(OnWalkNote, self).clean()
        if self.notification_type in OnWalkNote.RATING_CHOICES and self.rating is None:
            raise ValidationError({'rating': 'Value of type of notification should be have the rating set'})
        elif self.notification_type==ALERT and self.note is None:
            raise ValidationError({'note': 'Value of type of notification should be have a note populated'})
