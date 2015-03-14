import uuid

from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core import validators
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# from common.models import UUIDField
from feedback.models import Badge


class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    Username, password and email are required. Other fields are optional.
    """
    username = models.CharField(
        default=uuid.uuid4,
        max_length=36,
        unique=True,
        validators=[
            validators.RegexValidator(r'^[\w-]+$',
                                      _('Enter a valid username. '
                                        'This value may contain only letters, numbers '
                                        'and @/./+/-/_ characters.'), 'invalid'),
        ],
        error_messages={
            'unique': _("A user with that slug already exists."),
        }
    )
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    # TODO: Replace UUIDField when adpoting Django 1.8
    phone_number = models.CharField(
        max_length=11,
        validators=[
            validators.RegexValidator(r'^[\d]+$', ('Enter a valid phone number. '), 'invalid'),
        ],
        unique=True,
    )
    email = models.EmailField(_('email address'))
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'phone_number']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)


class ProfileBase(models.Model):
    '''
    Abstract class

    '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    address = models.TextField(blank=True)
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
