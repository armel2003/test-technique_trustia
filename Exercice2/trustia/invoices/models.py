from decimal import Decimal

from django.db import models

from products.models import Product


class Invoice(models.Model):
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "-id"]

    def __str__(self):
        return f"Facture #{self.pk}"

    def total(self) -> Decimal:
        """Somme des totaux par ligne (prix × quantité)."""
        total = Decimal("0")
        for item in self.items.select_related("product").all():
            total += item.line_total()
        return total

    def total_quantity(self) -> int:
        """Somme des quantités (nombre total d’articles)."""
        return sum(item.quantity for item in self.items.all())


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
        related_name="items",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="invoice_items",
    )
    quantity = models.PositiveIntegerField()

    class Meta:
        ordering = ["id"]

    def line_total(self) -> Decimal:
        """Total pour cette ligne : prix unitaire × quantité."""
        return self.product.prix * self.quantity
