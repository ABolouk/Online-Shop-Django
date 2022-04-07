from rest_framework import serializers

from .models import OrderItem, Order


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'number']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer', 'address', 'is_paid', 'off_code']
