nb_lignes , nb_mots = input().split()
nb_trouve = [0] * int(nb_mots)
phrase_1 = input().split()




print("{} {} {}".format(mots, " : ", nb_trouve[mots]))



### SOLUTION ###
nbLignes, nbMots = map(int, input().split(" "))
apparition = [0] * 101

for loop in range(nbLignes):
    texte = input().split(" ")
    
    for loop in range(nbMots):
        texte[loop] = len(texte[loop])

        for fois in range(101):
            if texte[loop] == fois:
                apparition[fois] = apparition[fois] + 1

for loop in range(101):
    if apparition[loop] > 0:
        print("{} : {}".format(loop, apparition[loop]))


# réunir 2 boucles en 1 ::
# for loop in range(nbMots):
#    idTexte = len(texte[loop])
#    apparition[idTexte] = apparition[idTexte] + 1