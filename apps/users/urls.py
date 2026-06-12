from django.urls import path

from apps.users.api_endpoints.users.UserList.views import user_list_view
from apps.users.api_endpoints.users.UserCreate.views import user_create_view
from apps.users.api_endpoints.users.UserDetail.views import user_detail_view
from apps.users.api_endpoints.users.UserUpdateDestroy.views import user_update_destroy_view


urlpatterns = [
    path('', user_list_view, name='user_list_view'),
    path('create/', user_create_view, name='user_create_view'),
    path('<int:pk>/', user_detail_view, name='user_detail_view'),
    path('<int:pk>/update/', user_update_destroy_view, name='user_update_destroy_view'),
    path('<int:pk>/delete/', user_update_destroy_view, name='user_update_destroy_view'),
]