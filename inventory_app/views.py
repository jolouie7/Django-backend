from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (CategorySerializer, ItemSerializer, UserSerializer)
from .models import (Category, Item, User)

# * should seprate into different views

# get all categories
@api_view(["GET"])
def categoryList(request):
  categories = Category.objects.all().order_by("id")
  serializer = CategorySerializer(categories, many=True)
  return Response(serializer.data)

# get one category
@api_view(["GET"])
def categoryDetail(request, pk):
  category = Category.objects.get(id=pk)
  serializer = CategorySerializer(category, many=False)
  return Response(serializer.data)

# create a category
@api_view(["POST"])
def categoryCreate(request):
  serializer = CategorySerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

# update a category
@api_view(["POST"])
def categoryUpdate(request, pk):
  categories = Category.objects.get(id=pk)
  serializer = CategorySerializer(instance=categories, data=request.data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data)

# delete one category
@api_view(["DELETE"])
def categoryDelete(request, pk):
  category = Category.objects.get(id=pk)
  category.delete()
  return Response("Category successfully deleted!")

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

