from datetime import timedelta
import uuid

from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core import validators
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import ShortUUIDField

from feedback.models import Badge


class User(AbstractBaseUser, PermissionsMixin):
    """
    The Pawtrol custom user.

    AbstractBaseUser provides the additional fields
        password = models.CharField(_('password'), max_length=128)
        last_login = models.DateTimeField(_('last login'), blank=True, null=True)
        is_active = True

    PermissionsMixin provides the additional fields
        is_superuser = models.BooleanField(_('superuser status'), default=False,
            help_text=_('Designates that this user has all permissions without '
                        'explicitly assigning them.'))
        groups = models.ManyToManyField(Group, verbose_name=_('groups'),
            blank=True, help_text=_('The groups this user belongs to. A user will '
                                    'get all permissions granted to each of '
                                    'their groups.'),
            related_name="user_set", related_query_name="user")
        user_permissions = models.ManyToManyField(Permission,
            verbose_name=_('user permissions'), blank=True,
            help_text=_('Specific permissions for this user.'),
            related_name="user_set", related_query_name="user")

    """
    username = ShortUUIDField(
        unique=True,
        error_messages={
            'unique': _("A user with that slug already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
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


class UserProfile(models.Model):
    '''
    UserProfile containing the information associated with the user which isn't important to authentication

    '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    address = models.TextField(blank=True)
    avatar = models.ImageField(blank=True)

    badges = models.ManyToManyField(Badge)


class OwnerProfile(models.Model):
    '''
    OwnerProfile used to store owner specific information for a user

    '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    preferred_walkers = models.ManyToManyField('WalkerProfile')


class ServiceBusiness(models.Model):
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

    uuid = ShortUUIDField(
        unique=True,
        error_messages={
            'unique': _("A business with that UUID already exists."),
        },
    )

    business_name = models.CharField(_('business name'), blank=False, null=False, max_length=200)
    business_owner = models.ForeignKey(
        'User',
        help_text=_('Setup so that a business can be assoiciated to any user regardless of whether they have a business profile')
    )

    subscription_status = models.CharField(max_length=10, choices=SUBSCRIPTION_STATUS_CHOICES, default=TRIAL)
    subscription_expiration_date = models.DateTimeField(_('date subscription expires'), default=timezone.now)


class ServiceProviderProfileBase(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    businesses = models.ManyToManyField('ServiceBusiness')

    class Meta:
        abstract = True


class WalkerProfile(ServiceProviderProfileBase):
    '''
    WalkerProfile used to store walker specific information for a user

    '''
    default_rate_per_hour_walked = models.DecimalField(max_digits=4, decimal_places=1, default=20)

    def __init__(self, *args, **kwargs):
        super(WalkerProfile, self).__init__(*args, **kwargs)
        self.subscription_expiration_date = timezone.now() + timedelta(days=60)
