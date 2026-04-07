from datetime import date
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from products.models import Product

from .models import Invoice, InvoiceItem


class InvoiceModelTests(TestCase):
    def test_total_and_line_total(self):
        p = Product.objects.create(
            nom="A",
            prix=Decimal("2.50"),
            date_peremption=date(2026, 6, 1),
        )
        inv = Invoice.objects.create()
        InvoiceItem.objects.create(invoice=inv, product=p, quantity=3)
        item = inv.items.first()
        self.assertEqual(item.line_total(), Decimal("7.50"))
        self.assertEqual(inv.total(), Decimal("7.50"))
        self.assertEqual(inv.total_quantity(), 3)


class InvoiceViewsTests(TestCase):
    def setUp(self):
        self.p1 = Product.objects.create(
            nom="P1",
            prix=Decimal("10.00"),
            date_peremption=date(2026, 6, 1),
        )
        self.p2 = Product.objects.create(
            nom="P2",
            prix=Decimal("3.00"),
            date_peremption=date(2026, 6, 1),
        )

    def test_invoice_create_and_detail(self):
        url = reverse("invoice_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            url,
            {
                "items-TOTAL_FORMS": "2",
                "items-INITIAL_FORMS": "0",
                "items-MIN_NUM_FORMS": "0",
                "items-MAX_NUM_FORMS": "1000",
                "items-0-product": str(self.p1.pk),
                "items-0-quantity": "2",
                "items-1-product": str(self.p2.pk),
                "items-1-quantity": "1",
            },
        )
        self.assertEqual(response.status_code, 302, response.content)
        inv = Invoice.objects.get()
        self.assertEqual(inv.total(), Decimal("23.00"))
        detail = self.client.get(reverse("invoice_detail", args=[inv.pk]))
        self.assertEqual(detail.status_code, 200)
        self.assertContains(detail, "23")

    def test_invoice_list(self):
        Invoice.objects.create()
        response = self.client.get(reverse("invoice_list"))
        self.assertEqual(response.status_code, 200)
