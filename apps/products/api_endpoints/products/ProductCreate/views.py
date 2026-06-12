from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.products.api_endpoints.products.ProductCreate.serializers import ProductCreateSerializer
from apps.products.models import Product

@api_view(['POST'])
def product_create_view(request):
    serializer = ProductCreateSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = 201)