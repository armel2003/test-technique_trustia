# Exercice 1 — Affichage de blocs en Python

## 📌 Description

Ce programme Python affiche des blocs de texte formatés dans la console avec des bordures.

Il respecte les contraintes suivantes :

* Largeur maximale configurable
* Texte affiché en minuscules
* Filtrage de certaines phrases non affichées
* Organisation flexible des blocs et de leur contenu

---

## 🧠 Fonctionnement

### 🔹 Stockage des données

Les blocs de texte sont stockés dans un dictionnaire `blocs`.
Chaque bloc contient une liste de phrases.

---

### 🔹 Filtrage intelligent

Les phrases à exclure sont définies dans la liste `phrases_interdites`.

Avant comparaison :

* Les phrases sont normalisées (minuscules + suppression des espaces inutiles)
* Cela permet d’éviter les erreurs liées à la casse ou aux espaces

---

### 🔹 Affichage des blocs

Chaque bloc est affiché avec :

* Une bordure supérieure et inférieure (`-`)
* Des bordures verticales (`|`)
* Un texte aligné automatiquement

---

### 🔹 Configuration

* `LARGEUR_MAX` permet de modifier facilement la largeur des blocs
* `ordre_affichage` permet de changer l’ordre d’affichage des blocs

---

## ▶️ Exécution

### Prérequis

* Python 3 installé

### Commande

```bash
python exercice1.py
```

ou

```bash
python3 exercice1.py
```

---

## 📁 Structure du projet

```
exercice1.py
README.md
```

---

## 🎯 Objectifs atteints

* Code simple et lisible
* Facilité de modification des données
* Séparation claire entre logique et contenu
* Respect des contraintes du test technique

---

## 💡 Améliorations possibles

* Gestion des lignes trop longues (retour à la ligne automatique)
* Ajout d’un centrage du texte
* Interface utilisateur (optionnel)

---

## 🏁 Conclusion

Ce projet démontre une implémentation propre et flexible d’un affichage structuré en console, tout en respectant les bonnes pratiques de développement.

