from rest_framework import serializers

from product.models import (
    Category,
    Product,
    Rating,
    Comment,
)


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


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
