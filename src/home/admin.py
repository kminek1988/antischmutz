from django.contrib import admin
from .models import *

@admin.register(SiteMeta)
class SiteMetaAdmin(admin.ModelAdmin):
    list_display = (
        "page_name",
        "title",
        "robots",
        "og_type",
        "theme_color",
   
    )

    search_fields = (
        "page_name",
        "title",
        "description",
        "keywords",
    )

    list_filter = (
        "robots",
        "og_type",
        "twitter_card",
    )

    fieldsets = (
        ("Podstawowe meta", {
            "fields": (
                "page_name",
                "title",
                "description",
                "keywords",
                "canonical_url",
                "robots",
            )
        }),
        ("Open Graph / Facebook", {
            "fields": (
                "og_title",
                "og_description",
                "og_image",
                "og_url",
                "og_type",
            )
        }),
        ("Twitter / X", {
            "fields": (
                "twitter_card",
                "twitter_title",
                "twitter_description",
                "twitter_image",
            )
        }),
        ("Wygląd / techniczne", {
            "fields": (
                "favicon",
                "theme_color",
            )
        }),
    )



admin.site.register(HeroSection)
admin.site.register(AboutSection)
admin.site.register(CtaSection)
