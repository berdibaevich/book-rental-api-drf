from rest_framework import serializers
from django.core.validators import MinValueValidator
from .models import Book, Category


def validate_unique_items(value: int):
    if len(value) != len(set(value)):
        raise serializers.ValidationError("Category IDs must not be duplicate!")
    return value


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length=255, allow_blank=False)
    
    description = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True
    )

    category_ids = serializers.ListField(
        child=serializers.IntegerField(validators=[MinValueValidator(1)]),
        write_only=True,
        allow_empty=False,
        validators=[validate_unique_items]
    )


    def create(self, validated_data):
        category_ids = validated_data.pop('category_ids')
        book = Book.objects.create(**validated_data)
        book.categories.set(category_ids) # Save category IDs
        return book


    def validate_category_ids(self, value):
        existing_categories_count = Category.objects.filter(id__in=value).count()
        if existing_categories_count != len(set(value)):
            raise serializers.ValidationError("Some category IDs do not exists.")
        return value

