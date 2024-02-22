from django.db import models
from product_app.models import Product


class Ad(models.Model):
    """
    Поля для рекламной кампании
    """
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    budget = models.IntegerField()

    def __str__(self):
        return self.name
