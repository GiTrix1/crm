from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Отображает услуги в админке
    """

    list_display = ["name", "description", "cost"]
    list_display_links = ["name"]
