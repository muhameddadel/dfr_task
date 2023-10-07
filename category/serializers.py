from rest_framework import serializers
from .models import Category
from product.models import Product  # Assuming your Product model is in a "product" app

class CategorySerializer(serializers.ModelSerializer):
    total_products = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'

    def get_total_products(self, obj):
        """
        Custom method to calculate and return the total number of products in the category.
        """
        return Product.objects.filter(category=obj).count()

    def to_representation(self, instance):
        """
        Override the to_representation method to include 'total_products' field
        only when viewing a single category (not when listing categories).
        """
        data = super(CategorySerializer, self).to_representation(instance)
        
        # Check if 'view' exists in the context and retrieve the action
        view = self.context.get('view')
        if view and view.action == 'retrieve':
            data['total_products'] = self.get_total_products(instance)
        
        return data