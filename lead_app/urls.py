from django.urls import path
from .views import (
    LeadsListView,
    LeadsCreateView,
    LeadsDetailView,
    LeadsDeleteView,
    LeadsUpdateView,
)

app_name = "lead_app"

urlpatterns = [
    path("", LeadsListView.as_view(), name="leads_list"),
    path("new/", LeadsCreateView.as_view(), name="leads_create"),
    path("<int:pk>/", LeadsDetailView.as_view(), name="leads_details"),
    path("<int:pk>/delete/", LeadsDeleteView.as_view(), name="leads_delete"),
    path("<int:pk>/edit/", LeadsUpdateView.as_view(), name="leads_edit"),
]
