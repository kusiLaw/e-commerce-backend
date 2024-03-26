from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from custom_users.models import User

# Create your models here.


class Color(models.Model):
    name = models.CharField(max_length=15,  unique=True)
    code = models.CharField(max_length=15, unique=True)

class Size(models.Model):
    text = models.CharField(max_length=15,  unique=True)
    unit = models.CharField(max_lenth=15, null=True, blank=True,
                            help_text='Handle at frontend since unit is not known ahead of time')


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length='120', blank=False, unique=True)
    product_code = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=False , null=False)
    created_at = models.DateTimeField( auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    quantity= models.IntegerField()
    cost_price = models.DecimalField(_("cp"), max_digits=5, decimal_places=2, blank=False, null=False)
    saling_price = models.DecimalField(_("sp"), max_digits=5, decimal_places=2, blank=False, null=False)
    color = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)
    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self) -> str:
        return self.name





        



