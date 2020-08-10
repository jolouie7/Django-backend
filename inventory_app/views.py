from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (CategorySerializer, ItemSerializer, UserSerializer)
from .models import (Category, Item, User)

# * should seprate into different views

# Get all categories
@api_view(["GET"])
def allCategories(request):
  categories = Category.objects.all()
  serializer = CategorySerializer(categories, many=True)
  return Response(serializer.data)

# Get all items
@api_view(["GET"])
def allItems(request):
  items = Item.objects.all()
  serializer = ItemSerializer(items, many=True)
  return Response(serializer.data)

# Get all users
@api_view(["GET"])
def allUsers(request):
  users = User.objects.all()
  serializer = UserSerializer(users, many=True)
  return Response(serializer.data)

