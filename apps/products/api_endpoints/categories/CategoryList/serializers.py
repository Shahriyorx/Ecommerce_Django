from rest_framework import serializers

from apps.products.models import Category

class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
