from account.models import Customer, Address
from store.models import Category, ProductType, ProductSpecification, ProductSpecificationValue
from checkout.models import DeliveryOptions, PaymentSelection

from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class ProductSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = '__all__'


class ProductSpecsValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecificationValue
        fields = '__all__'


class DeliveryOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryOptions
        fields = '__all__'


class PaymentSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentSelection
        fields = '__all__'
