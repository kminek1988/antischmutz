from django.shortcuts import render
from .models import *
from django.views.generic import DetailView

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'

    slug_field = 'slug'
    slug_url_kwarg = 'slug'