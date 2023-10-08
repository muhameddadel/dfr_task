from django.http import JsonResponse
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from django.db import transaction
import datetime

from .models import Product
from .serializers import ProductSerializer

from .exceptions import CategoryProductLimitExceeded  # Import the custom exception

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except CategoryProductLimitExceeded as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        if product:
            serializer = ProductSerializer(product, data=request.data, partial=True)

            try:
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)
            except CategoryProductLimitExceeded as e:
                return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# custom endpoint 
@api_view(['GET'])
def custom_product_list(request):
    if request.method == 'GET':
        today = datetime.date.today()
        queryset = Product.objects.filter(updated_at__date=today)
        total_price = queryset.aggregate(Sum('price'))['price__sum'] or 0
        count = queryset.count()

        product_data = [
            {'id': product.id, 'price': product.price}
            for product in queryset
        ]

        response_data = {
            'products': product_data,
            'total_price': total_price,
            'count': count,
        }
        return Response(response_data)