nb_x = int(input())
nb_ligne_rect = int(input())
nb_colonne_rect = int(input())
nb_triangle = int(input())

def ligne(nb_x) :
    print("X" * nb_x)

def rectangle (nb_ligne_rect, nb_colonne_rect):
    if nb_colonne_rect == 1 :
        for line in range(nb_ligne_rect):
            print("#")
    else :
        print("#"*nb_colonne_rect)
        for ligne in range (nb_ligne_rect-2) :
            print("#", " "*(nb_colonne_rect-4), "#")
        print("#"*nb_colonne_rect)

def triangle(nb_triangle):
    print("@")
    for ligne in range(0, nb_triangle-2) :
        print("@", end="")
        print(" "*ligne, end="")
        print("@", end="")
        print()
    print ("@"*nb_triangle)

ligne(nb_x)
print()
rectangle(nb_ligne_rect, nb_colonne_rect)
print()
triangle(nb_triangle)


### solution france ioi ::
# def ligne(longueur, motif):
#    for iCol in range(longueur):
#       print(motif, end = "")
#    print()
# def ligneCreuse(longueur, motif):
#    if longueur > 1:
#       print(motif, end = "")
#       for iEspace in range(longueur - 2):
#          print(" ", end = "")
#    print(motif)
# def rectangle(hauteur, largeur, motif):
#    if hauteur > 1:
#       ligne(largeur, motif)
#       for iLigne in range(hauteur - 2):
#          ligneCreuse(largeur, motif)
#    ligne(largeur, motif)
# def triangle(hauteur, motif):
#    for iLigne in range(1, hauteur):
#       ligneCreuse(iLigne, motif)
#    ligne(hauteur, motif)
# longueurLigne = int(input())
# ligne(longueurLigne, "X")
# print()
# hauteurRectangle = int(input())
# largeurRectangle = int(input())
# rectangle(hauteurRectangle, largeurRectangle, "#")
# print()
# hauteurTriangle = int(input())
# triangle(hauteurTriangle, "@")