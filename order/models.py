from django.db import models
from foods.models import Food


# Create your models here.

class Order(models.Model):
    order_id = models.CharField(max_length=200)
    order_number = models.CharField(max_length=200)
    table_number = models.CharField(max_length=20)


class OrderDetails(models.Model):
    orders = models.OneToOneField(Order, on_delete=models.CASCADE)
    food_name = models.OneToOneField(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    discount = models.FloatField(default=0.0)
