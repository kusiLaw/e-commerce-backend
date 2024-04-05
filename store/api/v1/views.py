from django.shortcuts import render
from rest_framework import viewsets, generics,  filters,status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ProductImageSerializer, ProductListSerializer, ProductDetailSerializer
from store.models import Product
from store.custom_pagination import CustomPageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .braintree import gateway


class ProductList(generics.ListAPIView):
    queryset = Product.objects.prefetch_related('product_image')
    serializer_class = ProductListSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]


    filterset_fields = ['name']
    search_fields = ['name']

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.prefetch_related(
        'color', 'size', 'product_image', 'category')
    serializer_class = ProductDetailSerializer

class GeneratePaymentToken(APIView):
    def get(self, request, format=None):
        try:
          client_token = gateway.client_token.generate()
        except:
            return Response(
                {'error' : 'Oops, something went wrong, server error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        return Response(
                {'token' : client_token},
            status=status.HTTP_200_OK

            )