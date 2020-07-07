joueur_1 = input()
joueur_2 = input()
nb_victoire_1 = 0
nb_victoire_2 = 0
nb_egalite = 0

for tour in range(52) :
    if joueur_1[tour] != "" or joueur_2[tour] != "" :
        if joueur_1[tour] > joueur_2[tour] :
            nb_victoire_1 +=1
        elif joueur_1[tour] < joueur_2[tour] :
            nb_victoire_2 +=1
        elif joueur_1[tour] == joueur_2[tour] :
            nb_egalite += 1


        if nb_victoire_1 > nb_victoire_2 :
            print("1")
            print(nb_egalite)
            
        elif nb_victoire_1 < nb_victoire_2 :
            print("2")
            print(nb_egalite)

