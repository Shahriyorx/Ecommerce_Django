from rest_framework import serializers

from apps.products.models import Category

class CategoryCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        