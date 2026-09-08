from rest_framework import serializers
from .models import Book, Category


class CategoryListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)



class BookListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    rental_rate = serializers.DecimalField(max_digits=8, decimal_places=2)


class BookDetailSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    pages = serializers.IntegerField()
    rental_duration = serializers.IntegerField()
    rental_rate = serializers.DecimalField(max_digits=8, decimal_places=2)
    replacement_cost = serializers.DecimalField(max_digits=8, decimal_places=2)
    created_at = serializers.DateTimeField()
    last_update = serializers.DateTimeField()
    categories = CategoryListSerializer(many=True)


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length=255, allow_blank=False)
    
    description = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True
    )
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        write_only=True,
        allow_empty=False
    )


    def create(self, validated_data):
        print("validated_data: ", validated_data)
        category_ids = validated_data.pop('category_ids')

        book = Book.objects.create(**validated_data)
        book.categories.set(category_ids)
        return book
    

