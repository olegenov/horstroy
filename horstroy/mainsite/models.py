from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    image = models.ImageField(upload_to="images", verbose_name="Картинка")

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("name", )

class Service(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="services", verbose_name="Картинка")
    gallery = models.ManyToManyField(
        Image,
        related_name='service_gallery',
        verbose_name="Галерея",
        null=True,
        blank=True,
    )

class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="services", verbose_name="Картинка")
    gallery = models.ManyToManyField(
        Image,
        related_name='project_gallery',
        verbose_name="Галерея"
    )

class DesignProject(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="services", verbose_name="Картинка")
    gallery = models.ManyToManyField(
        Image,
        related_name='design_project_gallery',
        verbose_name="Галерея"
    )
