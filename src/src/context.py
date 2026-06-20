from documents.models import *
from services.models import *
from home.models import SiteMeta
from django.http import FileResponse
from django.shortcuts import get_object_or_404

def global_context(request):
    return {
        'impressum': Impressum.objects.first(),
        'datenschutz': Datenschutz.objects.first(),
        'company': CompanyData.objects.first(),
        'certificates': Certifikat.objects.all(),
        'services': Service.objects.all(),
        'site_meta': SiteMeta.objects.first(),
    }


def current_year(request):
    from datetime import datetime
    return {
        'current_year': datetime.now().year
    }