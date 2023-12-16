def somme_nombres_pairs(liste):
    somme = 0
    for nombre in liste:
        if nombre % 2 == 0:
            somme += nombre
    return somme

taille_list = int(input("Entrez le nombre d'éléments dans la liste : "))
ma_liste = [int(input("Entrez un entier : ")) for _ in range(taille_list)]

resultat = somme_nombres_pairs(ma_liste)
print("Somme des nombres pairs :", resultat)
