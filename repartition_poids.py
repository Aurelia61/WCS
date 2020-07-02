nb_charettes = int(input())

poids_charettes = [""] * nb_charettes
poids_total = 0
for charettes in range(nb_charettes) :
    poids = float(input())
    poids_total = poids +poids_total
    poids_charettes[charettes] = poids

poids_moyen = poids_total / nb_charettes

for num_charette in range(nb_charettes):
    poids_charettes[num_charette] = poids_moyen - poids_charettes[num_charette]
    print(poids_charettes[num_charette])

