from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.orders.api_endpoints.orders.OrderList.serializers import OrderSerializer
from apps.orders.models import Order

@api_view(['GET'])
def order_list_view(request):    
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)