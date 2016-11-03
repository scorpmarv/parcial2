from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from parcial.app.serializers import InvoiceSerializer
from parcial.app.models import Invoice


class InvoiceViewset(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
