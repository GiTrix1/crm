from django.contrib import admin
from .models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """
    Отображает продукт в админке
    """
    list_display = ['name', 'budget']
    list_display_links = ['name']
