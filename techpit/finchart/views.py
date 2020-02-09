from django.shortcuts import render

from django.views.generic import TemplateView
from .models import Fstatement


class IndexView(TemplateView):
    template_name = "finchart/index.html"

    def get_context_data(self, **kwargs):
        fstatement_list = Fstatement.objects.all().order_by('company')
        print(fstatement_list)

        params = {
            'fstatement_list': fstatement_list,
        }

        return params