from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from parcial.app.models import Invoice, InvoiceDetail


class InvoiceAPITestCase(APITestCase):
    fixtures = ['parcial/app/fixtures/fixtures.json']

    def test_get(self):
        invoice = Invoice.objects.first()
        self.assertIsNotNone(invoice)
        response = self.client.get(reverse('invoice-detail', args=(invoice.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('InvoiceNumber'), invoice.InvoiceNumber)
        self.assertEqual(len(response.data.get('InvoiceDetail')), invoice.InvoiceDetail.count())

    def test_post(self):
        data = {
            u'CustomerName': u'Empresa SRL',
            u'Date': u'2002-05-30T09:30:10-06:00',
            u'InvoiceDetail': [{u'ArticleId': 100,
                                u'ArticleName': u'Computer',
                                u'ArticlePrice': 1000},
                               {u'ArticleId': 150,
                                u'ArticleName': u'Hard drive',
                                u'ArticlePrice': 2000}],
            u'InvoiceNumber': 1001,
            u'InvoiceTotalValue': 2000
        }
        response = self.client.post(reverse('invoice-list'), data=data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get('InvoiceNumber'), data[u'InvoiceNumber'])
        self.assertEqual(len(response.data.get('InvoiceDetail')), len(data[u'InvoiceDetail']))
