from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import (
    product_list,
    create_new_product,
    category_list,
    ProductApiView,
    AllProductsGenericView,
    CategoryViewSet,
    RatingViewSet,
    CommentViewSet,
    InfoProductGenericView,
    UserViewSet,
    ProductsAllPIView,
    ProductInfoGenericView
)

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'rating', RatingViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('product/', product_list),
    path('product-create/', create_new_product),
    path('category-list/', category_list),
    path('products/', ProductApiView.as_view()),
    path('products/<int:product_id>/', AllProductsGenericView.as_view()),
    path('info-product/<int:product_id>/', InfoProductGenericView.as_view()),
    path('products-all/<int:product_id>/', ProductInfoGenericView.as_view()),
] + router.urls
