from django.db import models
from lead_app.models import Lead
from contract_app.models import Contract


class Customer(models.Model):
    """
    Поля для покупателя
    """

    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)

    def __str__(self):
        return self.lead.first_name
