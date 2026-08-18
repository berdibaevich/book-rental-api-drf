from rest_framework import serializers
from .models import Book, Category



class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length=255, allow_blank=False)
    
    description = serializers.CharField(
        required=False,
        allow_null=True,
        allow_blank=True
    )

    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        write_only=True,
        allow_empty=False
    )



    def create(self, validated_data):
        categories = validated_data.pop('categories', [])
        book = Book.objects.create(**validated_data)
        book.categories.set(categories)
        return book
    

