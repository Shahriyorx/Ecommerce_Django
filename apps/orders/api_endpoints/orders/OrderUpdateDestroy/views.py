from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.orders.api_endpoints.orders.OrderUpdateDestroy.serializers import OrderUpdateDestroySerializer
from apps.orders.models import Order

@api_view(['PATCH', 'DELETE'])
def order_update_destroy_view(request, pk):
    try:
        order = Order.objects.get(pk = pk)
    except Order.DoesNOtExist:
        return Response({'error': 'Order not found'}, status = 404)
    
    if request.method == 'PATCH':
        serializer = OrderUpdateDestroySerializer(order, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        elif request.method == 'DELETE':
            order.delete()
            return Response(status = 204)