from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class Company(models.Model):
    title = models.CharField("Название", max_length=200)
    code = models.CharField("Код", max_length=15)
    description = RichTextUploadingField(null=True, blank=True)
    created_at = models.DateTimeField("Дата создания", default=timezone.now)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return self.title


class Stock(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    cost = models.FloatField("Стоимость")
    created_at = models.DateTimeField("Дата создания", default=timezone.now)

    class Meta:
        verbose_name = "Акция Компании"
        verbose_name_plural = "Акции Компании"

    def __str__(self):
        return f"{self.company} {self.pk}"
