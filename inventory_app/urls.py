from django.urls import path
from . import views

urlpatterns = [
  path("category-list/", views.categoryList, name="category-list"),
  path("category-detail/<str:pk>/", views.categoryDetail, name="category-detail"),
  path("category-create/", views.categoryCreate, name="category-create"),
  path("category-update/<str:pk>/", views.categoryUpdate, name="category-update"),
  path("category-delete/<str:pk>/", views.categoryDelete, name="category-delete"),
  path("items/", views.allItems, name="inven-items"),
  path("users/", views.allUsers, name="inven-users"),
]
