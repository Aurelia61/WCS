nb_emplacements = int(input())
liste_marchands = [""] * nb_emplacements

for emplacement in range (nb_emplacements):
    num_marchand = int(input())
    liste_marchands[emplacement] = num_marchand

liste_emplacement = [""] * nb_emplacements

for empl in range(nb_emplacements) :
    marchand = liste_marchands[empl]
    liste_emplacement[marchand] = empl

for marchand in range(nb_emplacements):  
    print(liste_emplacement[marchand])