from django.db import models

class Category(models.Model):
    name = models.JSONField()

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Categories'
