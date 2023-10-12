from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    #create category as foreign key
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    #method to get the product after click on product by product id
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)
     
    #method to get all product 
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    #method to get product after selecting category
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();