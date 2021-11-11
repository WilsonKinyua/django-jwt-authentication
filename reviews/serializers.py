from .models import Product, Category
from rest_framework import serializers

from django.contrib.auth.models import User
from django.utils.timezone import now


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']


class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer(Many=True)

    class Meta:
        model = Product
        # fields = ['pk', 'name', 'category']
        fields = '__all__'
        # read_only_fields = ['name']
        # exclude = ['category'] # pk and name to be serialized


class UserSerializer(serializers.ModelSerializer):
    days_since_joined = serializers.SerializerMethodField()

    class Meta:
        model = User

    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days
