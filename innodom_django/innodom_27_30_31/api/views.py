from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import (api_view, )
from django.contrib.auth.admin import User
from api.serializers import (
    AllProductsSerializers,
    CategorySerializers,
    RaitingSerializers,
    CommentSerializers,
    InfoProductSerializer,
    UserSerializers
)
from product.models import (
    Product,
    Category,
    Rating,
    Comment
)


@api_view(['GET'])
def product_list(request: Request):
    product = Product.objects.all()

    if product:
        serializer = AllProductsSerializers(
            instance=product,
            many=True
        )

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    return Response(
        status=status.HTTP_204_NO_CONTENT,
        data=[]
    )


# Домашнее задание 31
# Задание 3 Создайте функцию с декоратором @api_view(['GET']), которая позволяет получить список всех категорий из
# базы данных. Пользователи должны иметь возможность получить список всех категорий в формате JSON, используя метод GET.


@api_view(['GET'])
def category_list(request: Request):
    category = Category.objects.all()

    if category:
        serializer = CategorySerializers(
            instance=category,
            many=True
        )

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    return Response(
        status=status.HTTP_204_NO_CONTENT,
        data=[]
    )


@api_view(['POST'])
def create_new_product(request: Request):
    serializer = AllProductsSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(
            status=status.HTTP_201_CREATED,
            data=serializer.data
        )
    return Response(
        status=status.HTTP_400_BAD_REQUEST,
        data=serializer.errors
    )


from rest_framework.views import APIView, Request
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated


# Задание 31
# Задание 2
# Создайте APIView, которое позволяет получить список всех товаров из базы данных. Пользователи должны иметь \
# возможность получить список всех товаров в формате JSON, используя метод GET.

class ProductApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request):
        product = Product.objects.all()

        if product:
            serializer = AllProductsSerializers(instance=product, many=True)

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data=[]
        )

    def post(self, request: Request):
        try:
            serializer = AllProductsSerializers(
                data=request.data
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(
                status=status.HTTP_201_CREATED,
                data=serializer.data
            )
        except ValidationError as error:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    "error": str(error),
                    "detail": error.detail
                }
            )


from rest_framework.generics import (
    RetrieveAPIView,
    get_object_or_404,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)


class AllProductsGenericView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AllProductsSerializers

    def get_object(self):
        product_id = self.kwargs.get("product_id")

        product = get_object_or_404(Product, id=product_id)

        return product


class InfoProductGenericView(RetrieveAPIView):
    serializer_class = InfoProductSerializer

    def get_object(self):
        product_id = self.kwargs.get("product_id")

        product = get_object_or_404(Product, id=product_id)

        return product


from rest_framework.viewsets import ModelViewSet


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class RatingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Rating.objects.all()
    serializer_class = RaitingSerializers


class CommentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Comment.objects.all()
    serializer_class = CommentSerializers


# Задание 31
# Задание 1
# Создайте ViewSet, который позволяет получить список всех пользователей из базы данных. Пользователи должны иметь
# возможность получить список всех пользователей в формате JSON, используя метод GET.


class UserViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = User.objects.all()
    serializer_class = UserSerializers


# Домашнее 31
# Задание 4 Создайте GenericAPIView с использованием RetrieveUpdateDestroyAPIView, которое позволяет просматривать
# информацию об отдельной статье по её уникальному идентификатору (ID). Пользователи должны иметь возможность
# получить информацию о статье в формате JSON, используя метод GET, обновить данные статьи, используя метод PUT или
# PATCH, и удалить статью, используя метод DELETE.

class ProductInfoGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = AllProductsSerializers

    def update_subtask_info(self, instance):
        serializer = self.serializer_class(
            instance=instance,
            data=self.request.data
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data

    def get_object(self):
        subtask_id = self.kwargs.get('product_id')
        subtask = get_object_or_404(
            Product,
            id=subtask_id
        )

        return subtask

    def get(self, request: Request, *args, **kwargs):
        subtask = self.get_object()

        serializer = self.serializer_class(instance=subtask)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request: Request, *args, **kwargs):
        subtask = self.get_object()

        data = self.update_subtask_info(instance=subtask)

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "message": SUBTASK_SUCCESS_CREATED_MESSAGE,
                "data": data
            }
        )

    def delete(self, request, *args, **kwargs):
        subtask = self.get_object()

        subtask.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=SUBTASK_SUCCESS_DELETED_MESSAGE
        )


class ProductsAllPIView(ListCreateAPIView):
    serializer_class = AllProductsSerializers

    def get_queryset(self):
        product = Product.objects.all()
        return product

    def get(self, request: Request, *args, **kwargs):
        product = self.get_queryset()

        if not product:

            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data=[]
            )

        serializer = self.serializer_class(product, many=True)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )