from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)


class Subcategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category,  on_delete = models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    subcategory = models.ForeignKey(Subcategory, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
