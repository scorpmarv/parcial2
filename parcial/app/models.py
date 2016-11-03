from __future__ import unicode_literals

from django.db import models


class Invoice(models.Model):
    InvoiceNumber = models.BigIntegerField(primary_key=True)
    Date = models.DateTimeField()
    CustomerName = models.CharField(max_length=100)
    InvoiceTotalValue = models.FloatField()


class InvoiceDetail(models.Model):
    InvoiceNumber = models.ForeignKey(Invoice, related_name="InvoiceDetail")
    ArticleId = models.BigIntegerField()
    ArticleName = models.CharField(max_length=100)
    ArticlePrice = models.FloatField()
