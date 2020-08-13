
# ne fonctionne pas
nb_lignes , nb_mots = map(int,input().split(" "))
nb_trouve = [0] * 101

for loop in range(nb_lignes) :
    phrase = input().split()
    for loop in range(nb_mots) :
        phrase[loop] = len(phrase[loop])
        for mot in range(101) :
            if phrase[loop] == mot :
                nb_trouve[mot] += 1

for mot in range(101) :
    if nb_trouve[mot] > 0 :
        print("{} : {}".format(mot, nb_trouve[mot]))


### SOLUTION ###
histogramme = [0] * 101
for loop in range(nbLignes):
   mots = input().split(" ")
   for idMot in range(nbMots):
      longueur = len(mots[idMot])
      histogramme[longueur] = histogramme[longueur] + 1
for longueur in range(101):
   if histogramme[longueur] > 0:
      print("{} : {}".format(longueur, histogramme[longueur]))

# nbLignes, nbMots = map(int, input().split(" "))
# apparition = [0] * 101

# for loop in range(nbLignes):
#     texte = input().split(" ")
    
#     for loop in range(nbMots):
#         texte[loop] = len(texte[loop])

#         for fois in range(101):
#             if texte[loop] == fois:
#                 apparition[fois] = apparition[fois] + 1

# for loop in range(101):
#     if apparition[loop] > 0:
#         print("{} : {}".format(loop, apparition[loop]))


# réunir 2 boucles en 1 ::
# for loop in range(nbMots):
#    idTexte = len(texte[loop])
#    apparition[idTexte] = apparition[idTexte] + 1