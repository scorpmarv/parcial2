from rest_framework.serializers import ModelSerializer
from parcial.app.models import Invoice, InvoiceDetail


class InvoiceDetailSerializer(ModelSerializer):
    class Meta:
        model = InvoiceDetail
        exclude = ('id', 'InvoiceNumber')


class InvoiceSerializer(ModelSerializer):
    InvoiceDetail = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = '__all__'

    def create(self, validated_data):
        details = validated_data.pop('InvoiceDetail', None)
        invoice = Invoice.objects.create(**validated_data)
        for detail in details:
            InvoiceDetail.objects.create(InvoiceNumber=invoice, **detail)
        return invoice
