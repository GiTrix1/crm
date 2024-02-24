from django.urls import path
from .views import (
    AdsListView,
    AdsCreateView,
    AdsDetailView,
    AdsDeleteView,
    AdsUpdateView,
    AdsStatListView,
)

app_name = "ad_app"

urlpatterns = [
    path("", AdsListView.as_view(), name="ads_list"),
    path("new/", AdsCreateView.as_view(), name="ads_create"),
    path("<int:pk>/", AdsDetailView.as_view(), name="ads_details"),
    path("<int:pk>/delete/", AdsDeleteView.as_view(), name="ads_delete"),
    path("<int:pk>/edit/", AdsUpdateView.as_view(), name="ads_edit"),
    path("statistic/", AdsStatListView.as_view(), name="ads_statistic"),
]
