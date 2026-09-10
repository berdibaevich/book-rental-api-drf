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
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    pages = serializers.IntegerField()
    rental_duration = serializers.IntegerField()
    rental_rate = serializers.DecimalField(max_digits=8, decimal_places=2)
    replacement_cost = serializers.DecimalField(max_digits=8, decimal_places=2)
    created_at = serializers.DateTimeField()
    last_update = serializers.DateTimeField()
    categories = CategoryListSerializer(many=True)



class BookCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_null=True, allow_blank=False)
    pages = serializers.IntegerField(required=True, min_value=30)
    rental_duration = serializers.IntegerField(default=7, min_value=2)
    rental_rate = serializers.DecimalField(max_digits=8, decimal_places=2, min_value=0)
    replacement_cost = serializers.DecimalField(max_digits=8, decimal_places=2, min_value=0)
    category_ids = serializers.ListField(
        required=True,
        write_only=True,
        allow_empty=False,
        child=serializers.IntegerField()
        )
    

    default_error_messages = {
        'category_not_found': 'IDs were not found: {invalid_ids}'
    }

    def create(self, validated_data):
        category_ids = validated_data.pop("category_ids")
        book = Book.objects.create(**validated_data)
        book.categories.set(category_ids)
        return book


    def validate_category_ids(self, value):
        unique_ids = set(value)
        existing_ids = set(Category.objects.filter(id__in=unique_ids).values_list('id', flat=True))
        invalid_ids = list(unique_ids - existing_ids)

        if invalid_ids:
            raise serializers.ValidationError(
                self.error_messages['category_not_found'].format(invalid_ids=invalid_ids),
                code='category_not_found'
            )
        return value

