from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from .models import Lead


class LeadsListView(ListView):
    """
    Выводит список лидов
    """
    template_name = 'leads/leads-list.html'
    model = Lead
    context_object_name = 'leads'


class LeadsCreateView(PermissionRequiredMixin, CreateView):
    """
    Создает лида
    """
    permission_required = 'lead_app.add_lead'
    template_name = 'leads/leads-create.html'
    model = Lead
    fields = 'first_name', 'last_name', 'phone', 'email', 'ad'
    success_url = reverse_lazy('lead_app:leads_list')


class LeadsDetailView(PermissionRequiredMixin, DetailView):
    """
    Детальная информация о лиде
    """
    permission_required = 'lead_app.view_lead'
    template_name = 'leads/leads-detail.html'
    model = Lead
    context_object_name = 'leads'


class LeadsDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Удаляет лида
    """
    permission_required = 'lead_app.delete_lead'
    template_name = 'leads/leads-delete.html'
    model = Lead
    success_url = reverse_lazy('lead_app:leads_list')


class LeadsUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Редактирует лида
    """
    permission_required = 'lead_app.change_lead'
    template_name = 'leads/leads-edit.html'
    model = Lead
    fields = 'first_name', 'last_name', 'phone', 'email', 'ad'
    success_url = reverse_lazy('lead_app:leads_list')
