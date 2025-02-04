from django.db import models


class Order(models.Model):
    product_id = models.IntegerField(("Production ID"), blank=True, null=True)
    user_id = models.IntegerField(("User ID"), blank=True, null=True)
    quantity = models.IntegerField(("Quantity"), blank=True, null=True)
    created_at = models.DateTimeField(("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(("Updated At"), auto_now=True)

    def __str__(self):
        return self.product_id if self.product_id else self.id
