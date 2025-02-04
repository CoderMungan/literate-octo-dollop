from django.db import models


class Production(models.Model):
    name = models.CharField(("Name"), max_length=255, blank=True, null=True)
    price = models.IntegerField(("Price"), blank=True, null=True)
    created_at = models.DateTimeField(("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(("Updated At"), auto_now=True)

    def __str__(self) -> str:
        return self.name
