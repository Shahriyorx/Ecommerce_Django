from rest_framework.decorators import api_view
from rest_framework.response import Response 

from apps.users.api_endpoints.users.UserDetail.serializers import UserDetailSerializer
from apps.users.models import User

@api_view(['GET'])
def user_detail_view(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserDetailSerializer(user)
    return Response(serializer.data)