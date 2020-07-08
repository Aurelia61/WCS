longueur_dentelle = int(input())

def dentelle (carac, longueur) :
    print(carac * longueur)

dentelle("X",longueur_dentelle)
dentelle("#",longueur_dentelle)
dentelle("i",longueur_dentelle)


# ### solution france ioi ::
# def ligneDentelle(longueur, motif):
#     for iCol in range(longueur):
#         print(motif, end = "");
#     print()
# longueur = int(input())
# ligneDentelle(longueur, "X");
# ligneDentelle(longueur, "#");
# ligneDentelle(longueur, "i");