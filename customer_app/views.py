from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from .models import Customer


class CustomersListView(LoginRequiredMixin, ListView):
    """
    Выводит список покупателей
    """
    template_name = 'customers/customers-list.html'
    model = Customer
    context_object_name = 'customers'


class CustomersCreateView(PermissionRequiredMixin, CreateView):
    """
    Создает покупателя
    """
    permission_required = 'customer_app.add_customer'
    template_name = 'customers/customers-create.html'
    model = Customer
    fields = 'lead', 'contract'
    success_url = reverse_lazy('customer_app:customers_list')


class CustomersDetailView(PermissionRequiredMixin, DetailView):
    """
    Удаляет покупателя
    """
    permission_required = 'customer_app.view_customer'
    template_name = 'customers/customers-detail.html'
    model = Customer
    context_object_name = 'customers'


class CustomersDeleteView(DeleteView):
    """
    Детальная информация о покупателе
    """
    template_name = 'customers/customers-delete.html'
    model = Customer
    success_url = reverse_lazy('customer_app:customers_list')


class CustomersUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Редактирует покупателя
    """
    permission_required = 'customer_app.change_customer'
    template_name = 'customers/customers-edit.html'
    model = Customer
    fields = 'lead', 'contract'
    success_url = reverse_lazy('customer_app:customers_list')
