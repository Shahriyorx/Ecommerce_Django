from django.urls import path

from apps.products.api_endpoints.products.ProductCreate.views import product_create_view
from apps.products.api_endpoints.products.CategoryCreate.views import category_create_view
from apps.products.api_endpoints.products.ProductDetail.views import product_detail_view
from apps.products.api_endpoints.products.ProductUpdateDestroy.views import product_update_destroy_view
from apps.products.api_endpoints.products.ProductList.views import product_list
from apps.products.views import get_products

urlpatterns = [
    path('', product_list, name='product_list'),
    path('create/', product_create_view, name='product_create_view'),
    path('category_create/', category_create_view, name='category_create_view'),
    path('<int:pk>/', product_detail_view, name = 'product_detail_view'),
    path('<int:pk>/update/', product_update_destroy_view, name = 'product_update_destroy_view'),
    path('<int:pk>/delete/', product_update_destroy_view, name = 'product_update_destroy_view'),
]