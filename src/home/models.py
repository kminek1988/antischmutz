from django.db import models


class SiteMeta(models.Model):
    page_name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nazwa strony"
    )

    title = models.CharField(
        max_length=255,
        verbose_name="Meta title"
    )

    description = models.TextField(
        max_length=500,
        verbose_name="Meta description"
    )

    keywords = models.TextField(
        blank=True,
        null=True,
        verbose_name="Meta keywords"
    )

    canonical_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Canonical URL"
    )

    robots = models.CharField(
        max_length=100,
        default="index, follow",
        verbose_name="Robots"
    )

    og_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Open Graph title"
    )

    og_description = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Open Graph description"
    )

    og_image = models.ImageField(
        upload_to="meta/og/",
        blank=True,
        null=True,
        verbose_name="Open Graph image"
    )

    og_url = models.URLField(
        blank=True,
        null=True,
        verbose_name="Open Graph URL"
    )

    og_type = models.CharField(
        max_length=50,
        default="website",
        verbose_name="Open Graph type"
    )

    twitter_card = models.CharField(
        max_length=50,
        default="summary_large_image",
        verbose_name="Twitter card"
    )

    twitter_title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Twitter title"
    )

    twitter_description = models.TextField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Twitter description"
    )

    twitter_image = models.ImageField(
        upload_to="meta/twitter/",
        blank=True,
        null=True,
        verbose_name="Twitter image"
    )

    favicon = models.ImageField(
        upload_to="meta/favicon/",
        blank=True,
        null=True,
        verbose_name="Favicon"
    )

    theme_color = models.CharField(
        max_length=20,
        default="#000000",
        verbose_name="Theme color"
    )

   

    class Meta:
        verbose_name = "Meta strony"
        verbose_name_plural = "Meta stron"

    def __str__(self):
        return self.page_name


    def save(self, *args, **kwargs):
        if SiteMeta.objects.count() > 0 and self.pk is None:
            raise ValueError("Only one SiteMeta instance is allowed")
        super().save(*args, **kwargs)



class HeroSection(models.Model):
       
    image1 = models.ImageField(
        upload_to="hero/",
        verbose_name="Image 1",
        blank=True,
        null=True
    )
    image3 = models.ImageField(
        upload_to="hero/",
        verbose_name="Image 3",
        blank=True,
        null=True
    )
    image2 = models.ImageField(
        upload_to="hero/",
        verbose_name="Image 2",
        blank=True,
        null=True
    )
    title1 = models.CharField(
        max_length=255,
        verbose_name="Title 1",
        blank=True,
        null=True
    )
    title2 = models.CharField(
        max_length=255,
        verbose_name="Title 2",
        blank=True,
        null=True
    )
 
    class Meta:
        verbose_name = "Hero section"
        verbose_name_plural = "Hero sections"
    
    def __str__(self):
        return 'hero'

    def save(self, *args, **kwargs):
        if HeroSection.objects.count() > 0 and self.pk is None:
            raise ValueError("Only one HeroSection instance is allowed")
        super().save(*args, **kwargs)


class AboutSection(models.Model):
    image = models.ImageField(
        upload_to="about/",
        verbose_name="Image",
        blank=True,
        null=True
    )
    content = models.TextField(
        verbose_name="Content",
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = "O firmie"
        verbose_name_plural = "O firmie"
    
    def __str__(self):
        return "O firmie"

    def save(self, *args, **kwargs):
        if AboutSection.objects.count() > 0 and self.pk is None:
            raise ValueError("Only one AboutSection instance is allowed")
        super().save(*args, **kwargs)
    
class CtaSection(models.Model):
    banner = models.ImageField(
        upload_to="cta/",
        verbose_name="Banner",
        blank=True,
        null=True
    )
    content = models.TextField(
        verbose_name="Content",
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = "CTA"
        verbose_name_plural = "CTA"
    
    def __str__(self):
        return "CTA"
    
    def save(self, *args, **kwargs):
        if CtaSection.objects.count() > 0 and self.pk is None:
            raise ValueError("Only one CtaSection instance is allowed")
        super().save(*args, **kwargs)
    


    
