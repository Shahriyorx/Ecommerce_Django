from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.users.api_endpoints.users.UserCreate.serializers import UserCreateSerializers
from apps.users.models import User

@api_view(['POST'])
def user_create_view(request):
    serializer = UserCreateSerializers(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
