from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
from django.utils import timezone
# Create your models here.

   
class User(AbstractUser):
    """
      overwrite some AbstractUser properties and replace username with email and add additional fields.

      email, password, first and last name are required. Other fields are optional.
    """
    username = None
    first_name = models.CharField(_("first name"), max_length=150, blank=False, null=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False, null=False)
    email = models.EmailField(_("email address"), blank=False, null=False, unique=True,
                              help_text="Email is required" , max_length=150,
                              error_messages={ "unique": _("A user with that username already exists."),},
                              )
   
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    is_active = models.BooleanField(default=False)
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]


    objects = CustomUserManager()

    class Meta: 
      ordering = ['-date_joined',]


    @property
    def token(self):
      pass





