from django.urls import path
from .views import (CustomersListView, CustomersCreateView, CustomersDetailView, CustomersDeleteView,
                    CustomersUpdateView)

app_name = 'customer_app'

urlpatterns = [
    path('', CustomersListView.as_view(), name='customers_list'),
    path('new/', CustomersCreateView.as_view(), name='customers_create'),
    path('<int:pk>/', CustomersDetailView.as_view(), name='customers_details'),
    path('<int:pk>/delete/', CustomersDeleteView.as_view(), name='customers_delete'),
    path('<int:pk>/edit/', CustomersUpdateView.as_view(), name='customers_edit'),
]
