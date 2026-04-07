from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("nom", "prix", "date_peremption")
    search_fields = ("nom",)
