lettre = input()
nb_lignes = int(input())
nombre =0

for loop in range(nb_lignes) :
    ligne = input()
    nombre += ligne.count(lettre)

print(nombre)



### solution France IOI ::
# lettre = input()
# nbLignes = int(input())
# nbFois = 0
# for loop in range(nbLignes):
#    ligne = input()
#    for idLettre in range(len(ligne)):
#        if ligne[idLettre] == lettre:
#           nbFois = nbFois + 1
# print(nbFois)