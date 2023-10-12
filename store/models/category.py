from django.db import  models

class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod  #static Method to get all categories
    def get_all_categories():
        return Category.objects.all()

    #constructor that convert the category object to string
    def __str__(self):
        return self.name
