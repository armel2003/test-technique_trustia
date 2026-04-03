blocs = {
    "bloc1": [
        "Le code propre facilite la maintenance"
    ],
    "bloc2": [
        "Tester souvent evite beaucoup d erreurs",
        "Cette phrase ne doit pas s afficher"
        ],
    "bloc3": [
        "Cette phrase ne doit pas s afficher",
        "Un bon code doit rester simple et claire",
        "La simplicite ameliore la qualite du code",
        "Refactoriser ameliore la comprehension"
        ],
}

phrases_interdites = [
    "Cette phrase ne doit pas s afficher",
    "Un bon code doit rester simple et claire"
]

LARGEUR_MAX = 90

def afficher_bloc(lignes):
    phrases_interdites_normalisees = {p.strip().lower() for p in phrases_interdites}
    lignes_filtrees = []
    for ligne in lignes:
        if ligne.strip().lower() not in phrases_interdites_normalisees:
            lignes_filtrees.append(ligne.strip().lower())

    largeur_texte = LARGEUR_MAX - 2
    print("-" * LARGEUR_MAX)

    for ligne in lignes_filtrees:
        print("|" + ligne.rjust(largeur_texte) + "|")

    print("-" * LARGEUR_MAX)

ordre_affichage = ["bloc1", "bloc2", "bloc3"]

if __name__ == "__main__":
    for bloc in ordre_affichage:
        afficher_bloc(blocs[bloc])