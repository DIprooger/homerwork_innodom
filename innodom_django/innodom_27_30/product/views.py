from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product, Category
from product.forms import CreateProductForm, ProductUpdateForm


def home_page(request):
    return render(
        request=request,
        template_name='main.html'
    )


def get_all_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(
        request=request,
        template_name='product/all_products.html',
        context=context
    )


def create_new_product(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            product_data = form.cleaned_data
            Product.objects.create(**product_data)
            return redirect("product:all-product")
        context = {
            'form': form,
            'categories': categories
        }
    else:
        form = CreateProductForm()
        context = {
            'form': form,
            'categories': categories
        }

    return render(
        request=request,
        template_name='product/create_product.html',
        context=context
    )


def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()

    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect("product:all-product")

        context = {
            'form': form,
            'categories': categories
        }

    else:
        form = ProductUpdateForm(instance=product)
        context = {
            'form': form,
            'categories': categories
        }

    return render(
        request=request,
        template_name='product/create_product.html',
        context=context
    )


def get_product_info_by_product_id(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    contex = {
        'product': product
    }

    return render(
        request=request,
        template_name='product/product_info.html',
        context=contex
    )


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    product.delete()
    return redirect('product:all-product')
