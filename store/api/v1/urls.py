from django.urls import path, include
from .views import ProductList, ProductDetail, GeneratePaymentToken

urlpatterns = [
   path('products/', ProductList.as_view(), name='product-list'),
   path('products/<int:pk>/',
        ProductDetail.as_view(), name='product-detail'),
   path('products/payment-token', GeneratePaymentToken.as_view(), name='payment-token'),

   # path('products/checkout/',),
   # path('products/checkout/payment/',)
]
