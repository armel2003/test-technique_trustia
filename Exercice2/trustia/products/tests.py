from datetime import date
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Product


class ProductViewsTests(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            nom="Test",
            prix=Decimal("10.50"),
            date_peremption=date(2026, 12, 31),
        )

    def test_product_list_pagination(self):
        url = reverse("product_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test")

    def test_product_crud_flow(self):
        create_url = reverse("product_create")
        response = self.client.post(
            create_url,
            {
                "nom": "Nouveau",
                "prix": "5.00",
                "date_peremption": "2027-01-15",
            },
        )
        self.assertEqual(response.status_code, 302)
        p = Product.objects.get(nom="Nouveau")
        self.assertEqual(p.prix, Decimal("5.00"))

        edit_url = reverse("product_edit", args=[p.pk])
        response = self.client.post(
            edit_url,
            {
                "nom": "Nouveau bis",
                "prix": "6.00",
                "date_peremption": "2027-01-15",
            },
        )
        self.assertEqual(response.status_code, 302)
        p.refresh_from_db()
        self.assertEqual(p.nom, "Nouveau bis")

        delete_url = reverse("product_delete", args=[p.pk])
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Product.objects.filter(pk=p.pk).exists())
