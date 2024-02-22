from django.db import models


class Product(models.Model):
    """
    Поля для услуги
    """
    name = models.CharField(max_length=50)
    description = models.TextField(null=False, blank=True)
    cost = models.IntegerField()

    def __str__(self):
        return self.name
