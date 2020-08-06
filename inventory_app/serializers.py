from rest_framework import serializers
from .models import (User, Item, Category)

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = "__all__"

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = "__all__"