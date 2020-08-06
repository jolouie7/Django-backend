from django.db import models
from django import forms

# Create your models here.

# def validate_greater_than_zero(value):
#     if value < 0:
#         raise ValidationError(
#             _('%(value)s is less then 0'),
#             params={'value': value},
#         )
class Category(models.Model):
  name = models.CharField(max_length=200)
  # items in the 1 category
  category_quantity = models.IntegerField(
    default=0,
  )

  def __str__(self):
    return self.name

class Item(models.Model):
  name = models.CharField(max_length=200)
  category_id = models.ForeignKey("Category", on_delete=models.CASCADE)
  description = models.CharField(max_length=200)
  # picture can change to ImageField later
  picture = models.CharField(max_length=200)
  item_quantity = models.IntegerField(
    default=0,
  )
  user_id = models.ForeignKey("User", on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class User(models.Model):
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  # picture can change to ImageField later
  profile_picture = models.CharField(max_length=200)
  job_title = models.CharField(max_length=200)
  # If this forms.CharField....... doesn't work maybe do this
  # https://stackoverflow.com/questions/17523263/how-to-create-password-field-in-model-django
  # https://code.djangoproject.com/wiki/PasswordField ------code below------
  password = forms.CharField(max_length=50, widget=forms.PasswordInput)

  def __str__(self):
    return self.name