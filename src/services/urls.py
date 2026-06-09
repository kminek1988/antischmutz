from django.urls import path
from .views import *

urlpatterns = [
    path('angebot/<slug:slug>/', ServiceDetailView.as_view(), name='service_detail'),
]