from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm
from .models import Product

PAGE_SIZE = 10


def product_list(request):
    qs = Product.objects.all()
    paginator = Paginator(qs, PAGE_SIZE)
    page = paginator.get_page(request.GET.get("page"))
    return render(request, "products/product_list.html", {"page_obj": page})


def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit créé.")
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "products/product_form.html", {"form": form, "title": "Nouveau produit"})


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit mis à jour.")
            return redirect("product_list")
    else:
        form = ProductForm(instance=product)
    return render(
        request,
        "products/product_form.html",
        {"form": form, "title": f"Modifier « {product.nom} »"},
    )


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        try:
            product.delete()
        except ProtectedError:
            messages.error(
                request,
                "Impossible de supprimer ce produit : il est utilisé dans une facture.",
            )
            return redirect("product_list")
        messages.success(request, "Produit supprimé.")
        return redirect("product_list")
    return render(
        request,
        "products/product_confirm_delete.html",
        {"product": product},
    )
