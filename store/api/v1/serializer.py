from rest_framework import serializers
from store.models import ProductImage, Product, ProductColor, ProductSize


class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = ProductImage
        fields = ['image',]


class ProductSizesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductSize
        fields = ['size', 'unit']


class ProductColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductColor
        fields = ['color', 'color_code']


class ProductListSerializer(serializers.ModelSerializer):
    color = ProductColorSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail', read_only=True)

    product_image = ProductImageSerializer(
        many=True,
        read_only=True,
    )


    class Meta:
        model = Product
        fields = [ 'id', 'url','name', 'product_code',
                  'description', 
                  'tag', 'price', 'color', 'product_image']
        # depth = 2
      

class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
    size = ProductSizesSerializer(many=True, read_only=True)
    color = ProductColorSerializer(many=True, read_only=True)
    product_image = ProductImageSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Product
        fields = ['id', 'url', 'name', 'product_code',
                  'description', 'created_at', 'quantity',
                  'tag', 'price', 'color', 'size', 'product_image']
