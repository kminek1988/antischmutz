from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from services.models import *
from documents.models import *


class HomeView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["site_meta"] = SiteMeta.objects.first()
        context['hero'] = HeroSection.objects.first()
        context["about_section"] = AboutSection.objects.first()
        context["cta_section"] = CtaSection.objects.first()
        context["services"] = Service.objects.all()
        context["button1"] = Service.objects.first()
        context["button2"] = Service.objects.last()

        return context

class AboutView(TemplateView):
    template_name = "about.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about_section"] = AboutSection.objects.first()
        return context