from django.contrib import admin
from .models import Product, ProductColor, ProductImage, ProductSize, Category
from custom_users.models import User
# Register your models here.


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductColor)
admin.site.register(ProductSize)
admin.site.register(Category)
admin.site.register(User)
