from django.urls import path
from .views import (ProductsListView, ProductsDetailView, ProductsCreateView, ProductsDeleteView, ProductsUpdateView)

app_name = 'product_app'

urlpatterns = [
    path('', ProductsListView.as_view(), name='products_list'),
    path('new/', ProductsCreateView.as_view(), name='products_create'),
    path('<int:pk>/', ProductsDetailView.as_view(), name='products_details'),
    path('<int:pk>/delete/', ProductsDeleteView.as_view(), name='products_delete'),
    path('<int:pk>/edit/', ProductsUpdateView.as_view(), name='products_edit'),
]
