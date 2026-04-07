from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("nom", "prix", "date_peremption")
        widgets = {
            "nom": forms.TextInput(attrs={"class": "form-control"}),
            "prix": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.01", "min": "0.01"}
            ),
            "date_peremption": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
        }

    def clean_nom(self):
        nom = (self.cleaned_data.get("nom") or "").strip()
        if not nom:
            raise forms.ValidationError("Le nom est obligatoire.")
        return nom

    def clean_prix(self):
        prix = self.cleaned_data["prix"]
        if prix <= 0:
            raise forms.ValidationError("Le prix doit être strictement positif.")
        return prix
