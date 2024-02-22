from django.db import models
from ad_app.models import Ad


class Lead(models.Model):
    """
    Поля для лидов
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
