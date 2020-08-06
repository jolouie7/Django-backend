from django.urls import path
from . import views

urlpatterns = [
  path("", views.allCategories, name="inven-categories"),
]
