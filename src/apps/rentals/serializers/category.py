from rest_framework import serializers
from ..models import Category



class CategoryListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        library = self.context['library']
        return Category.objects.bulk_create([Category(library=library, **item) for item in validated_data])



class CategoryListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        list_serializer_class = CategoryListSerializer

