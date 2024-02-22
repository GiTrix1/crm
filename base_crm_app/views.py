from django.shortcuts import render
from django.views.generic import View


class BaseView(View):
    """
    Выводит базовый шаблон
    """

    def get(self, request):
        """
        :param request:
        :return: base template
        """
        return render(request, '_base.html')
