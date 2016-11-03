from django.contrib import admin
from parcial.app.models import Invoice, InvoiceDetail


class InvoiceDetailInline(admin.StackedInline):
    model = InvoiceDetail


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = (InvoiceDetailInline,)
