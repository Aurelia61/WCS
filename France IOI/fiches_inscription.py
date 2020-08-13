nb_personnes = int(input())

for personne in range(nb_personnes) :
    prenom_nom = input().split(" ")
    prenom = prenom_nom[0]
    nom = prenom_nom[1]
    print(nom+prenom)
