from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from .models import Product


class ProductsListView(LoginRequiredMixin, ListView):
    """
    Выводит список услуг
    """
    template_name = 'products/products-list.html'
    model = Product
    context_object_name = 'products'


class ProductsCreateView(PermissionRequiredMixin, CreateView):
    """
    Добавляет услугу
    """
    permission_required = 'product_app.add_product'
    template_name = 'products/products-create.html'
    model = Product
    fields = 'name', 'description', 'cost'
    success_url = reverse_lazy('product_app:products_list')


class ProductsDetailView(PermissionRequiredMixin, DetailView):
    """
    Детальная информация об услуге
    """
    permission_required = 'product_app.view_product'
    template_name = 'products/products-detail.html'
    model = Product
    context_object_name = 'products'


class ProductsUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Редактирует услугу
    """
    permission_required = 'product_app.change_product'
    template_name = 'products/products-edit.html'
    model = Product
    fields = 'name', 'description', 'cost'
    success_url = reverse_lazy('product_app:products_list')


class ProductsDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Удаляет услугу
    """
    permission_required = 'product_app.delete_product'
    template_name = "products/products-delete.html"
    model = Product
    success_url = reverse_lazy('product_app:products_list')
