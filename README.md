## Test technique — Trustia

Ce dépôt contient **2 exercices**.

- **Exercice 1** : script Python (console) d’affichage de blocs texte.
- **Exercice 2** : application web **Django + SQLite** de gestion de produits et de factures (avec pagination).

---

## Exercice 1 — Affichage de blocs en Python

### Emplacement
- Code : `exercice1.py` (à la racine)

### Objectif
Afficher des blocs de texte dans la console avec :
- **largeur max configurable**
- **texte en minuscules**
- **filtrage** de certaines phrases
- affichage avec **bordures** (`-` et `|`) et **alignement**

### Exécuter

```bash
python3 exercice1.py
```

---

## Exercice 2 — Django (Produits + Factures)

### Emplacement
- Projet : `Exercice2/trustia/`
- Virtualenv : `Exercice2/venv/`
- Base SQLite : `Exercice2/trustia/db.sqlite3`

### Modèles
- **Product** : `nom`, `prix`, `date_peremption`
- **Invoice** : `date` (auto)
- **InvoiceItem** : `invoice`, `product`, `quantity`

Règles métier :
- **total ligne** = \(prix \times quantité\) (méthode `InvoiceItem.line_total()`)
- **total facture** = somme des lignes (méthode `Invoice.total()`)

### URLs
- `/products/` : liste produits (paginée)
- `/products/create/` : créer produit
- `/products/edit/<id>/` : modifier produit
- `/products/delete/<id>/` : supprimer produit
- `/invoices/` : liste factures (paginée)
- `/invoices/create/` : créer facture (plusieurs lignes via formset)
- `/invoices/<id>/` : détail facture

### Lancer en local

Depuis la racine du dépôt :

```bash
cd Exercice2/trustia
../venv/bin/python manage.py migrate
../venv/bin/python manage.py runserver
```

Ouvrir ensuite `http://127.0.0.1:8000/`.

Note : si vous êtes dans `Exercice2/` (et pas dans `Exercice2/trustia/`), la commande correcte est :

```bash
venv/bin/python trustia/manage.py runserver
```

### Tests

```bash
cd Exercice2/trustia
../venv/bin/python manage.py test products invoices
```

---

## Remarques
- **Pagination** : activée sur les listes produits et factures.
- **UI** : templates simples (Bootstrap via CDN) + messages Django.
- **SQLite** : base par défaut Django.

