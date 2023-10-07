from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, value):
        """
        Custom validation for the 'price' field.
        Ensures that 'price' is greater than or equal to 0.
        """
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than or equal to 0.")
        return value

    def create(self, validated_data):
        # Convert the product name to lowercase before creating the product
        validated_data['name'] = {k: v.lower() if isinstance(v, str) else v for k, v in validated_data['name'].items()}
        
        return super(ProductSerializer, self).create(validated_data)


