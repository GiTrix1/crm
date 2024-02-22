from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Отображает покупателей в админке
    """
    list_display = ['lead']
