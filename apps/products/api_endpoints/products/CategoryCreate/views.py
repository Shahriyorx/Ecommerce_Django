from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.api_endpoints.products.CategoryCreate.serializers import CategoryCreateSerializers
from apps.products.models import Category

@api_view(['POST'])
def category_create_view(request):
    serializer = CategoryCreateSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)