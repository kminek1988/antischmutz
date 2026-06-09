from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nazwa", null=True, blank=True)
    slug = models.SlugField(max_length=255, verbose_name="Slug", null=True, blank=True)
    description = models.TextField(verbose_name="Opis", null=True, blank=True)
    image = models.ImageField(upload_to='services/', verbose_name="Obrazek", null=True, blank=True)
    hero_tekst = models.TextField(verbose_name="Tekst hero", null=True, blank=True)
    banner = models.ImageField(upload_to='services/', verbose_name="Baner", null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Usługa"
        verbose_name_plural = "Usługi"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("service_detail", kwargs={"slug": self.slug})


class Images(models.Model):
    service = models.ManyToManyField(Service, related_name="images", blank=True)
    image1 = models.ImageField(upload_to='services/', verbose_name="Zdjęcie przed", null=True, blank=True)
    image2 = models.ImageField(upload_to='services/', verbose_name="Zdjęcie po", null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name="Tytuł", null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Zdjęcie"
        verbose_name_plural = "Zdjęcia"