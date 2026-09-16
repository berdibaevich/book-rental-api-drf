from rest_framework import serializers

from .models import Book, Category


class CategoryListSerializer(serializers.ListSerializer):
    def validate(self, attrs):
        names = [item['name'] for item in attrs]
        
        if len(names) != len(set(names)):
            raise serializers.ValidationError("Duplicate name!")
        
        existing_in_db = set(
            Category.objects.filter(name__in=names).values_list("name", flat=True)
        )
 
        if existing_in_db:
            raise serializers.ValidationError(
                f"Categories already exist: {list(existing_in_db)}"
            )
        return attrs
    
    
    def create(self, validated_data):
        return Category.objects.bulk_create([Category(**item) for item in validated_data])



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        list_serializer_class = CategoryListSerializer
        extra_kwargs = {
            "name": {
                'validators': []
            }
        }




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
