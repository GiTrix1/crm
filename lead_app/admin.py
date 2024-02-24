from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    """
    Отображает лидов в админке
    """

    list_display = ["first_name", "last_name", "phone", "email"]
    list_display_links = ["first_name"]
