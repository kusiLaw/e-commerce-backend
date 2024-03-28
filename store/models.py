from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from custom_users.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=45,  unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
        ]

class ProductColor(models.Model):
    name = models.CharField(max_length=15,  unique=True)
    code = models.CharField(max_length=15, unique=True)

    def __str__(self) -> str:
        return self.name
    

class ProductSize(models.Model):
    text = models.CharField(max_length=15,  unique=True)
    unit = models.CharField(max_length=15, null=True, blank=True,
                            help_text='Handle at frontend since unit is not known ahead of time')

    def __str__(self) -> str:
        return self.text


class Product(models.Model):
    Tag = [
        ("new", "new"),
        ("hot", "hot"),
        ("sales", "sales"),
        ("default", "default"),
    ]

    name = models.CharField(max_length=120, blank=False, unique=True)
    product_code = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=255, blank=False , null=False)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity= models.PositiveIntegerField()
    tag = models.CharField(max_length=7, choices=Tag, default='default')
    cost_price = models.DecimalField(_("cp"), max_digits=5, decimal_places=2, blank=False, null=False)
    price = models.DecimalField(_("saling_price"),  max_digits=5, decimal_places=2, blank=False, null=False)
    color = models.ManyToManyField(ProductColor)
    size = models.ManyToManyField(ProductSize)
    user = models.ForeignKey(User, verbose_name=_(
        'product_owner'), on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
        indexes = [
            models.Index(fields=["name"]),
        ]
     

    def __str__(self) -> str:
        return self.name



class ProductImage(models.Model):
    image = image = models.ImageField(
        max_length=100, upload_to='store/static/')
    product = models.ForeignKey(Product, related_name='product_image', on_delete=models.CASCADE)




        



