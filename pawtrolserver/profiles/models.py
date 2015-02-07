from django.contrib.auth.models import User
from django.contrib.gis.db import models

from feedback.models import Badge


class ProfileBase(models.Model):
    '''
    Abstract class

    '''
    user = models.OneToOneField(User)

    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    avatar = models.ImageField(blank=True)

    date_last_seen = models.DateTimeField(auto_now_add=True)

    badges = models.ManyToManyField(Badge)

    class Meta:
        abstract = True


class OwnerProfile(ProfileBase):
    '''
    OwnerProfile used to store owner specific information for a user

    '''
    preferred_walkers = models.ManyToManyField('WalkerProfile')


class ServiceProviderProfileBase(ProfileBase):
    '''
    Abstract class

    Statuses:

    TRIAL           - The user is on a trial subscription (and not paying fees).
    ACTIVE          - The first payment for the subscription is successful. 
    DELINQUENT      - The subscription payment has failed, but the user is still in the grace period.
    SUSPENDED       - The subscription has been terminated, usually due to a payment issue. 
    UNSUBSCRIBED    - The walker has unsubscribed from the service.

    '''
    TRIAL = 'trial'
    ACTIVE = 'active'
    DELINQUENT = 'delinquent'
    SUSPENDED = 'suspended'
    UNSUBSCRIBED = 'unsubscribed'

    SUBSCRIPTION_STATUS_CHOICES = (
        (TRIAL, TRIAL),
        (ACTIVE, ACTIVE),
        (DELINQUENT, DELINQUENT),
        (SUSPENDED, SUSPENDED),
        (UNSUBSCRIBED, UNSUBSCRIBED),
    )

    subscription_status = models.CharField(max_length=10, choices=SUBSCRIPTION_STATUS_CHOICES)
    subscription_expiration_date = models.DateTimeField()

    class Meta:
        abstract = True


class WalkerProfile(ServiceProviderProfileBase):
    '''
    WalkerProfile used to store walker specific information for a user

    '''
    default_rate_per_walk = models.DecimalField(max_digits=4, decimal_places=1)
