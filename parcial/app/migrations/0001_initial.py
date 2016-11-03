# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-03 19:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('InvoiceNumber', models.BigIntegerField(primary_key=True, serialize=False)),
                ('Date', models.DateTimeField()),
                ('CustomerName', models.CharField(max_length=100)),
                ('InvoiceTotalValue', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ArticleId', models.BigIntegerField()),
                ('ArticleName', models.CharField(max_length=100)),
                ('ArticlePrice', models.FloatField()),
                ('InvoiceNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='InvoiceDetail', to='app.Invoice')),
            ],
        ),
    ]