from rest_framework import serializers

from .models import Book, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"




class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')



class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'id', 
            'title', 
            'rental_rate', 
            'pages',
            'last_update'
        )


class BookDetailSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(many=True)
    
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "description",
            "pages",
            "rental_duration",
            "rental_rate",
            "replacement_cost",
            "created_at",
            "last_update",
            "categories",
        )



class BookCreateUpdateSerializer(serializers.ModelSerializer):
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        allow_empty=False,
        many=True,
        source="categories"
    )

    class Meta:
        model = Book
        fields = (
            'id', 
            'title', 
            'description',
            'pages',
            'rental_duration',
            'rental_rate',
            'replacement_cost',
            'category_ids'
            )
        
        extra_kwargs = {
            "description": {'allow_null': True, 'allow_blank': False},
        }
