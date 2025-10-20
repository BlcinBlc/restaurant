from django.db import models

# Create your models here.

from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.TextField()
    phone = models.CharField(max_length=13)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menus')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=255)
    price = models.BigIntegerField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    address = models.TextField()

    def __str__(self):
        return self.username


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders')
    currency = models.CharField(max_length=10)

    def __str__(self):
        return f"Order {self.id} - {self.customer.username}"



class Driver(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.name
