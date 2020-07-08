joueur_1 = input()
joueur_2 = input()
minimum_cartes = min(len(joueur_1), len(joueur_2))
nb_victoire_1 = 0
nb_victoire_2 = 0
nb_egalite = 0

for tour in range(minimum_cartes) :
    if joueur_1[tour] < joueur_2[tour] :
        nb_victoire_1 +=1
        break
    elif joueur_1[tour] > joueur_2[tour] :
        nb_victoire_2 +=1
        break
    else:
        nb_egalite += 1

if nb_victoire_1 > nb_victoire_2 or (nb_victoire_1 == nb_victoire_2 and len(joueur_1) > len(joueur_2)):
    print("1")
elif nb_victoire_1 < nb_victoire_2 or (nb_victoire_1 == nb_victoire_2 and len(joueur_2) > len(joueur_1)) :
    print("2")
else:
    print("=")

print(nb_egalite)


### Solution France IOI ::
# main1 = input()
# main2 = input()
# tour = 0
# while tour < len(main1) and tour < len(main2) and main1[tour] == main2[tour]:
#     tour = tour + 1
# if tour == len(main1) and tour == len(main2):
#     print("=")
# elif tour == len(main2) or (tour < len(main1) and main1[tour] < main2[tour]):
#     print(1)
# else:
#     print(2)
# print(tour)

