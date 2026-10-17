from rest_framework import serializers
from ..models import Category



class CategoryListSerializer(serializers.ListSerializer):
    def validate(self, attrs):
        library = self.context['library']
        names = [item['name'] for item in attrs]

        if len(names) != len(set(names)):
            raise serializers.ValidationError("Failed: duplicated category!")

        existing_in_db = set(
            Category.objects.filter(library=library, name__in=names)
            .values_list("name", flat=True)
        )

        if existing_in_db:
            raise serializers.ValidationError(
                f"Failed: categories already exist: {list(existing_in_db)}"
            )
        return attrs


    def create(self, validated_data):
        library = self.context['library']
        return Category.objects.bulk_create([Category(library=library, **item) for item in validated_data])



class CategoryListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        list_serializer_class = CategoryListSerializer




class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

    def validate(self, attrs):
        library = self.context['library']
        name = attrs.get('name')

        if Category.objects.filter(library=library, name=name).exclude(pk=getattr(self.instance, 'pk', None)).exists():
            raise serializers.ValidationError(f"Failed: {name} already exist!")

        return super().validate(attrs)
