from rest_framework import serializers
from .models import Restaurant, Menu, Dish, Customer, Order, Driver

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name']


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ['name', 'price']
        depth =1


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username', 'phone']
        read_only_fields = ['restaurant']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'
