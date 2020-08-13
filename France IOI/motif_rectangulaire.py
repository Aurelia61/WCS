
nb_lignes = int(input())
nb_colonnes = int(input())
motif = input()

def feuille(motif_def, nb_colonnes_def, nb_lignes_def):
    for ligne in range(nb_lignes_def) :
        print(motif_def * nb_colonnes_def)

feuille(motif, nb_colonnes, nb_lignes)

### solution france ioi ::
# def dessinerRectangle(nbLignes, nbColonnes, motif):
#     for iLigne in range(nbLignes):
#         for iCol in range(nbColonnes):
#             print(motif, end = "")
#         print()
# nbLignes = int(input())
# nbColonnes = int(input())
# motif = input()
# dessinerRectangle(nbLignes, nbColonnes, motif)