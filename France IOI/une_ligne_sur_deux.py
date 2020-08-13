nb_lignes = int(input())
texte = [""] * nb_lignes

for ligne in range(nb_lignes):
    texte[ligne] = input()

for ligne in range(0, nb_lignes, 2):
    print (texte[ligne])
    