from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Product
from .exceptions import CategoryProductLimitExceeded

@receiver(pre_save, sender=Product)
def limit_products_per_category(sender, instance, **kwargs):
    # Check if the product already exists (has an ID)
    if instance.id:
        return 
    else:
        if instance.category.product_set.exclude(id=instance.id).count() >= 5:
            raise CategoryProductLimitExceeded("Cannot add more than 5 products to this category.")
