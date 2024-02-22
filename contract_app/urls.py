from django.urls import path
from .views import (ContractsListView, ContractsCreateView, ContractsDetailView, ContractsDeleteView,
                    ContractsUpdateView)

app_name = 'contract_app'

urlpatterns = [
    path('', ContractsListView.as_view(), name='contracts_list'),
    path('new/', ContractsCreateView.as_view(), name='contracts_create'),
    path('<int:pk>/', ContractsDetailView.as_view(), name='contracts_details'),
    path('<int:pk>/delete/', ContractsDeleteView.as_view(), name='contracts_delete'),
    path('<int:pk>/edit/', ContractsUpdateView.as_view(), name='contracts_edit'),
]
