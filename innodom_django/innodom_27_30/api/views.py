from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import (api_view,)

from api.serializers import (
    AllProductsSerializers,
    CategorySerializers,
    RaitingSerializers,
    CommentSerializers,
    InfoProductSerializer
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
