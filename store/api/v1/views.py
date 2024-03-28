from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializer import ProductImageSerializer, ProductListSerializer, ProductDetailSerializer
from store.models import Product
# Create your views here.


class ProductList(generics.ListAPIView):
    queryset = Product.objects.prefetch_related('product_image')
    serializer_class = ProductListSerializer


