from django.contrib import admin
from .models import Impressum, Datenschutz, CompanyData, Certifikat

admin.site.register(Impressum)
admin.site.register(Datenschutz)
admin.site.register(CompanyData)
admin.site.register(Certifikat)

# Register your models here.
