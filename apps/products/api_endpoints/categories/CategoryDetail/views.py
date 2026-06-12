from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.api_endpoints.categories.CategoryDetail.serializers import CategoryDetailSerializers
from apps.products.models import Category

@api_view(['GET'])
def category_detail_view(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        serializers = CategoryDetailSerializers(category)
        return Response(serializers.data)
    except Category.DoesNotExist:
        return Response({'error':'Category not found'} , status=404)
