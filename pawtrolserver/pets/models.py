from django.contrib.gis.db import models

from feedback.models import Badge
from profiles.models import WalkerProfile, OwnerProfile


class Pet(models.Model):
    """
    The Pet Model

    """

    DOG = 'dog'
    CAT = 'cat'
    SPECIES_CHOICES = (
        (DOG, 'Dog'),
        (CAT, 'Cat'),
    )

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

    name = models.CharField(max_length=255)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    dob = models.DateField()
    is_dob_estimated = models.BooleanField(default=False)

    # TODO: These should be choices for ease of sorting
    primary_breed = models.CharField(max_length=255)
    secondary_breed = models.CharField(max_length=255, blank=True)
    primary_coat_color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    secondary_coat_color = models.CharField(max_length=10, choices=COLOR_CHOICES, blank=True)
    coat_pattern = models.CharField(max_length=10, choices=PATTERN_CHOICES)
    description = models.TextField(blank=True)
    weight = models.DecimalField(max_digits=4, decimal_places=1)
    microchip_number = models.CharField(max_length=255)
    avatar = models.ImageField(blank=True)
    vet_name = models.CharField(max_length=255, blank=True)
    vet_number = models.CharField(max_length=11, blank=True)
    date_joined = models.DateTimeField(blank=True, null=True)

    badges = models.ManyToManyField(Badge)
    owner = models.ForeignKey(OwnerProfile)


class Pack(models.Model):
    """
    A model to associate a Walker to group of Pets

    """

    name = models.CharField(max_length=255)

    leader_profile = models.ForeignKey(WalkerProfile)
    pets = models.ManyToManyField('Pet')
