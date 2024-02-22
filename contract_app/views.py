from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from .models import Contract


class ContractsListView(ListView):
    """
    Выводит список контрактов
    """
    template_name = 'contracts/contracts-list.html'
    model = Contract
    context_object_name = 'contracts'


class ContractsCreateView(PermissionRequiredMixin, CreateView):
    """
    Создает контракт
    """
    permission_required = 'contract_app.add_contract'
    template_name = 'contracts/contracts-create.html'
    model = Contract
    fields = 'name', 'product', 'start_date', 'end_date', 'cost', 'documents'
    success_url = reverse_lazy('contract_app:contracts_list')


class ContractsDetailView(PermissionRequiredMixin, DetailView):
    """
    Детальная информация о контракте
    """
    permission_required = 'contract_app.view_contract'
    template_name = 'contracts/contracts-detail.html'
    model = Contract
    context_object_name = 'contracts'


class ContractsDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Удаляет контракт
    """
    permission_required = 'contract_app.delete_contract'
    template_name = 'contracts/contracts-delete.html'
    model = Contract
    success_url = reverse_lazy('contract_app:contracts_list')


class ContractsUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Редактирует контракт
    """
    permission_required = 'contract_app.change_contract'
    template_name = 'contracts/contracts-edit.html'
    model = Contract
    fields = 'name', 'product', 'start_date', 'end_date', 'cost'
    success_url = reverse_lazy('contract_app:contracts_list')
