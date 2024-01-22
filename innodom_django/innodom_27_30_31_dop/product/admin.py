from django.contrib import admin
from product.models import Product, Category, Rating, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Rating)
admin.site.register(Comment)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at')
