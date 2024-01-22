from django.urls import path
from product.views import (
    get_all_products,
    create_new_product,
    update_product,
    get_product_info_by_product_id,
    delete_product
)

app_name = 'product'

urlpatterns = [
    path('', get_all_products, name='all-product'),
    path('create/', create_new_product, name='create-product'),
    path('<int:product_id>/', get_product_info_by_product_id, name='product-info'),
    path('<int:product_id>/update/', update_product, name='update-product'),
    path('<int:product_id>/delete/', delete_product, name='delete-product'),
]
