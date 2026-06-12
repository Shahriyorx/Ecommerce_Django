from rest_framework.decorators import api_view
from rest_framework.response import Response    

from apps.users.api_endpoints.users.UserUpdateDestroy.serializers import UserUpdateDestroySerializer
from apps.users.models import User

@api_view(['PATCH', 'DELETE'])
def user_update_destroy_view(request, pk):
    try:
        user = User.objects.get(pk = pk)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)
    
    if request.method == 'PATCH':
        serializer = UserUpdateDestroySerializer(user, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    if request.method == 'DELETE':
        user.delete()
        return Response( status=200)