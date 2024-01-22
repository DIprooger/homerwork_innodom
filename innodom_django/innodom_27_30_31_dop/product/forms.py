from product.models import Category, Product
from django.forms import (
    ModelForm,
    fields,
    ModelChoiceField,
)


class CreateProductForm(ModelForm):
    name = fields.CharField(max_length=50)
    category = ModelChoiceField(queryset=Category.objects.all())
    prise = fields.CharField(max_length=50)

    class Meta:
        model = Product
        fields = '__all__'


class ProductUpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'prise')
