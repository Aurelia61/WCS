nb_x = int(input())
nb_ligne_rect = int(input())
nb_colonne_rect = int(input())
nb_triangle = int(input())

def ligne(nb_x) :
    print("*" * nb_x)

def rectangle (nb_ligne_rect, nb_colonne_rect):
    print("#"*nb_colonne_rect)
    for ligne in range (nb_ligne_rect-2) :
        print("#", " "*(nb_colonne_rect-4), "#")
    print("#"*nb_colonne_rect)

def triangle(nb_triangle):
    print("@")
    for ligne in range(0, nb_triangle-2) :
        print("@", end="")
        print(" "*ligne)
        print("@", end="")
        print()
    print ("@"*nb_triangle)

ligne(nb_x)
print()
rectangle(nb_ligne_rect, nb_colonne_rect)
print()
triangle(nb_triangle)