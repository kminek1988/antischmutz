from django.urls import path
from .views import *

urlpatterns = [
    path("impressum/", ImpressumView.as_view(), name="impressum"),
    path("datenschutz/", DatenschutzView.as_view(), name="datenschutz"),
]
