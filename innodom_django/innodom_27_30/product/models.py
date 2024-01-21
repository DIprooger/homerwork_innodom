from django.db import models
from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.name


class Rating(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

    def __str__(self):
        return self.rating


class Comment(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )
    rating = models.ManyToManyField(Rating, related_name='rating')
    comments = models.ManyToManyField(Comment, related_name='comment')
    prise = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
