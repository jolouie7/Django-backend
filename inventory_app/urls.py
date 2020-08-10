from django.urls import path
from . import views

urlpatterns = [
  path("categories/", views.allCategories, name="inven-categories"),
  path("items/", views.allItems, name="inven-items"),
  path("users/", views.allUsers, name="inven-users"),
]
