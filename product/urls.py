from django.urls import path
from .views import *


app_name = 'product'

urlpatterns = [
    path('', product_list, name='product-list'),
    path('custom/', custom_product_list, name='custom-product-list'),
    path('<int:pk>/', product_detail, name='product-detail'),
]
