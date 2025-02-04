from rest_framework import viewsets
from apps.production.models import Production
from apps.production.serializers import ProductionSerializer


class ProductionViewSet(viewsets.ModelViewSet):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer
