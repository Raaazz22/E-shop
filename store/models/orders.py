from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    #create product as foreign key
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    #create customer as foreign key
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    #function to save the place order
    def placeOrder(self):
        self.save()

    #method to get order of customer that shows in order
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
        #here -date return the order in descending order

