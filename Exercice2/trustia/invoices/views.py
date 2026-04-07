from django.contrib import messages
from django.core.paginator import Paginator
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .forms import InvoiceItemFormSet
from .models import Invoice

PAGE_SIZE = 10


def invoice_list(request):
    qs = Invoice.objects.prefetch_related("items__product").all()
    paginator = Paginator(qs, PAGE_SIZE)
    page = paginator.get_page(request.GET.get("page"))
    return render(request, "invoices/invoice_list.html", {"page_obj": page})


@transaction.atomic
def invoice_create(request):
    invoice = Invoice()
    if request.method == "POST":
        formset = InvoiceItemFormSet(request.POST, instance=invoice)
        if formset.is_valid():
            invoice.save()
            formset.instance = invoice
            formset.save()
            messages.success(request, "Facture créée.")
            return redirect("invoice_detail", pk=invoice.pk)
    else:
        formset = InvoiceItemFormSet(instance=invoice)
    return render(
        request,
        "invoices/invoice_form.html",
        {"formset": formset},
    )


def invoice_detail(request, pk):
    invoice = get_object_or_404(
        Invoice.objects.prefetch_related("items__product"),
        pk=pk,
    )
    items = list(invoice.items.all())
    line_count = len(items)
    total_qty = sum(i.quantity for i in items)
    return render(
        request,
        "invoices/invoice_detail.html",
        {
            "invoice": invoice,
            "items": items,
            "line_count": line_count,
            "total_qty": total_qty,
            "invoice_total": invoice.total(),
        },
    )
