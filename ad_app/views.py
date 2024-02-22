from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Sum
from django.views.generic import (DetailView, CreateView, DeleteView, UpdateView, ListView)
from django.urls import reverse_lazy
from contract_app.models import Contract
from customer_app.models import Customer
from lead_app.models import Lead
from .models import Ad


class AdsListView(ListView):
    """
    Выводит список всех рекламных компании
    """
    template_name = 'ads/ads-list.html'
    model = Ad
    context_object_name = 'ads'


class AdsCreateView(PermissionRequiredMixin, CreateView):
    """
    Создает рекламную компанию
    """
    permission_required = 'ad_app.add_ad'
    template_name = 'ads/ads-create.html'
    model = Ad
    fields = 'name', 'product', 'budget'
    success_url = reverse_lazy('ad_app:ads_list')


class AdsDetailView(PermissionRequiredMixin, DetailView):
    """
    Детальная информацию по рекламной компании
    """
    permission_required = 'ad_app.view_ad'
    template_name = 'ads/ads-detail.html'
    model = Ad
    context_object_name = 'ads'


class AdsUpdateView(PermissionRequiredMixin, UpdateView):
    """
    Редактирует рекламную компанию
    """
    permission_required = 'ad_app.change_ad'
    template_name = 'ads/ads-edit.html'
    model = Ad
    fields = 'name', 'product', 'budget'
    success_url = reverse_lazy('ad_app:ads_list')


class AdsDeleteView(PermissionRequiredMixin, DeleteView):
    """
    Удаляет рекламную компанию
    """
    permission_required = 'ad_app.delete_ad'
    template_name = 'ads/ads-delete.html'
    model = Ad
    success_url = reverse_lazy('ad_app:ads_list')


class AdsStatListView(ListView):
    """
    Выводит статистику о рекламной компании
    """
    template_name = 'ads/ads-statistic.html'
    model = Ad
    context_object_name = 'ads'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ads = context['ads']
        for ad in ads:
            ad.leads_count = Lead.objects.filter(ad__product_id=ad.product.pk).count()
            total_cost = Contract.objects.filter(product_id=ad.product.pk).aggregate(Sum('cost'))['cost__sum']
            if not total_cost:
                ad.profit = None
            else:
                ad.profit = round(total_cost / ad.budget, 2)
            ad.customers_count = Customer.objects.filter(contract__product_id=ad.product.pk).count()
        return context
