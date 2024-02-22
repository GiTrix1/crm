from django.contrib import admin
from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    """
    Отображает контракт в админке
    """
    list_display = ['name', 'start_date', 'end_date', 'cost']
    list_display_links = ['name']
