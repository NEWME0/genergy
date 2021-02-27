from django.utils.translation import ugettext_lazy as _
from django.db.models.enums import TextChoices
from django.db.models.fields import CharField, BooleanField, DateTimeField, FloatField, PositiveIntegerField
from django.db.models.query_utils import Q
from django.db.models.constraints import CheckConstraint
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator

from app_accounts.managers import UserManager


class Gender(TextChoices):
    male = 'MALE', _('male')
    female = 'FEMALE', _('female')


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    # Default user fields
    username = CharField(_('username'), max_length=150, unique=True, validators=[UnicodeUsernameValidator()])
    password = CharField(_('password'), max_length=128)
    fullname = CharField(_('fullname'), max_length=128, blank=True)
    is_staff = BooleanField(_('is staff'), default=False)
    last_login = DateTimeField(_('last login'), null=True)
    date_joined = DateTimeField(_('date joined'), auto_now_add=True)

    # Custom user fields
    idnp = CharField(_('idnp'), max_length=20, null=True, blank=True)
    phone = CharField(_('phone'), max_length=20, null=True, blank=True)
    gender = CharField(_('gender'), max_length=10, choices=Gender.choices, default=Gender.male.value)

    is_admin_account = BooleanField(_('is admin'), default=False)
    is_staff_account = BooleanField(_('is staff'), default=False)
    is_agent_account = BooleanField(_('is agent'), default=False)
    is_basic_account = BooleanField(_('is basic'), default=False)

    hour_price = FloatField(_('hour price'), default=100)
    agent_rate = PositiveIntegerField(_('agent rate'), default=10)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        constraints = [
            CheckConstraint(check=Q(gender__in=Gender.values), name='check_user_gender'),
            CheckConstraint(check=Q(agent_rate__lte=100), name='check_user_agent_rate'),
            CheckConstraint(check=Q(hour_price__gte=0), name='check_user_hour_price'),
        ]

    def email_user(self, subject, message, from_email=None, **kwargs):
        raise NotImplementedError("User model hasn't email")

    def get_full_name(self):
        return self.fullname

    def get_short_name(self):
        return self.fullname
