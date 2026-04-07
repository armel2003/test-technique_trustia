from django.db import models


class Product(models.Model):
    nom = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_peremption = models.DateField()

    class Meta:
        ordering = ["nom"]

    def __str__(self):
        return self.nom
