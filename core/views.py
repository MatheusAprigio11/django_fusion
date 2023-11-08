from typing import Any
from django.views.generic import TemplateView
from .models import Servico, Funcionario, Feature

class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self). get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['features'] = Feature.objects.all()
        return context



