from django.db import models
from product_app.models import Product


def path(instance: "Contract", filename):
    """
    Возвращает путь с именем файла
    """
    return f"{instance.name}/{filename}"


class Contract(models.Model):
    """
    Поля для контракта
    """

    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.IntegerField()
    documents = models.FileField(upload_to=path, null=False)

    def __str__(self):
        return self.name
