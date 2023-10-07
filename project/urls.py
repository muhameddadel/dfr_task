from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('product.urls', namespace='products')),
    path('categories/', include('category.urls', namespace='categories')),
]
