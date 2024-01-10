from django.db import models
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=30)


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Categoru,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )
    prise = models.IntegerField(max_length=10)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
