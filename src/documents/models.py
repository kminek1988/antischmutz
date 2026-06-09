from django.db import models

class Impressum(models.Model):
    content = models.TextField(
        verbose_name="Content",
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = "Impressum"
        verbose_name_plural = "Impressum"
    
    def __str__(self):
        return "Impressum"
    
    def save(self, *args, **kwargs):
        if Impressum.objects.count() > 0 and self.pk is None:
            raise ValueError("Only one Impressum instance is allowed")
        super().save(*args, **kwargs)

class Datenschutz(models.Model):
    content = models.TextField(
        verbose_name="Content",
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = "Datenschutz"
        verbose_name_plural = "Datenschutz"
    
    def __str__(self):
        return "Datenschutz"
    
    def save(self, *args, **kwargs):
        if Datenschutz.objects.count() > 0 and self.pk is None:
            raise ValueError("Only one Datenschutz instance is allowed")
        super().save(*args, **kwargs)


class CompanyData(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Nazwa firmy",
        blank=True,
        null=True
    )
    address = models.CharField(
        max_length=255,
        verbose_name="adres",
        blank=True,
        null=True
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="numer telefonu",
        blank=True,
        null=True
    )
    email = models.EmailField(
        verbose_name="Email",
        blank=True,
        null=True
    )
    logo = models.ImageField(
        verbose_name="Logo",
        blank=True,
        null=True
    )
    maps = models.TextField(
        verbose_name="Mapa",
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name="banner",
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = "Company Data"
        verbose_name_plural = "Company Data"
    
    def __str__(self):
        return "Company Data"
    
    def save(self, *args, **kwargs):
        if CompanyData.objects.count() > 0 and self.pk is None:
            raise ValueError("Only one CompanyData instance is allowed")
        super().save(*args, **kwargs)




class Certifikat(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Name",
        blank=True,
        null=True
    )
    file = models.FileField(
        verbose_name="File",
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = "Certyfikat"
        verbose_name_plural = "Certyfikaty"
    
    def __str__(self):
        return self.name


    