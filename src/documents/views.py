from django.shortcuts import render
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import *


class ImpressumView(TemplateView):
    template_name = "documents/impressum.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["impressum"] = Impressum.objects.first()
        return context


class DatenschutzView(TemplateView):
    template_name = "documents/datenschutz.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["datenschutz"] = Datenschutz.objects.first()
        return context


