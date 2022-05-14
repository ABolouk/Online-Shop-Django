from rest_framework import serializers

from product.models import Product, Brand, Discount, Category


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ['name', 'type', 'amount']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'price', 'image', 'detail', 'is_available', 'discount', 'category']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'is_parent']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']

# class ProductSerializer(serializers.Serializer):
#     def update(self, instance: Product, validated_data: dict):
#         instance.name = validated_data.get('name', instance.name)
#         instance.brand = validated_data.get('brand', instance.brand)
#         instance.image = validated_data.get('image', instance.image)
#         instance.detail = validated_data.get('detail', instance.detail)
#         instance.is_available = validated_data.get('is_available', instance.is_available)
#         instance.category = validated_data.get('category', instance.category)
#         return instance
#
#     def create(self, validated_data: dict):
#         return Product.objects.create(**validated_data)
#
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     # brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())
#     brand = serializers.StringRelatedField()
#     price = serializers.CharField(max_length=20)
#     image = serializers.ImageField(allow_empty_file=True)
#     detail = serializers.CharField(allow_null=True)
#     is_available = serializers.BooleanField(default=True)
#     # discount = serializers.PrimaryKeyRelatedField(queryset=Discount.objects.all())
#     discount = serializers.StringRelatedField()
#     # category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), allow_null=True)
#     category = serializers.StringRelatedField(many=True)
