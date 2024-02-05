from rest_framework import serializers
from product.models import (
    Category,
    Product,
    Rating,
    Comment,
)
from user.models import User
from api.error_messages import CATEGORY_NAME_LEN_ERROR_MESSAGE, PASSWORDS_DO_NOT_MATCH_ERROR


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


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68,
        min_length=8,
        write_only=True)
    password2 = serializers.CharField(
        max_length=68,
        min_length=8,
        write_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'password',
            'password2'
        ]

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError(
                PASSWORDS_DO_NOT_MATCH_ERROR
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            password=validated_data.get('password'),
        )
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'