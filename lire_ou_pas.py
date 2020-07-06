nb_livres = int(input())
longueur_max = 0

for livre in range(nb_livres) :
    titre = input()
    if len(titre) > longueur_max :
        longueur_max = len(titre)
        print(titre)



