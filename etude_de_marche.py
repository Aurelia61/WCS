nb_produits = int(input())
nb_personnes = int(input())

liste_produits = [0] * nb_produits

for personnes in range(nb_personnes) :
    num_produit = int(input())
    liste_produits[num_produit] += 1

print(*liste_produits, sep='\n')