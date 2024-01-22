from rest_framework import serializers
from django.contrib.auth.admin import User
from product.models import (
    Category,
    Product,
    Rating,
    Comment,
)


# Домашнее 30
# Напишите ModelSerializer для всех трёх моделей


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AllProductsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'category',
            'prise',
            'created_at',
            'language'
        ]


# домашнее 30
# Serializer реализуйте метод, который позволит пользователю ввести идентификатор товара, а
# затем вернет его рейтинг и список всех комментариев, связанных с этим товаром.


class InfoProductSerializer(serializers.ModelSerializer):
    rating_my = RatingSerializer(many=True, read_only=True, source='rating')
    comments_my = CommentSerializer(many=True, read_only=True, source='comments')

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'category',
            'prise',
            'rating_my',
            'comments_my'
        ]





from api.error_messages import CATEGORY_NAME_LEN_ERROR_MESSAGE


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 4 or len(value) > 25:
            raise serializers.ValidationError(
                CATEGORY_NAME_LEN_ERROR_MESSAGE
            )


class RaitingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
