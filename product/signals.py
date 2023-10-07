from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Product

@receiver(pre_save, sender=Product)
def limit_products_per_category(sender, instance, **kwargs):
    # Check if the category already has 2 products (customize this number as needed)
    if instance.category.product_set.count() >= 5:
        raise Exception("Cannot add more than 5 products to this category.")
