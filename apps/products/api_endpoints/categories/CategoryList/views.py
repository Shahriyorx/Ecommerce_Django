from rest_framework.decorators import api_view
from rest_framework.response import Response 

from apps.products.api_endpoints.categories.CategoryList.serializers import CategoryListSerializers
from apps.products.models import Category

@api_view(['GET'])
def category_list_view(request):
    categories = Category.objects.all()
    serializers = CategoryListSerializers(categories, many=True)
    return Response(serializers.data)
