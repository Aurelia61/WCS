
nb_positions = int(input())
nb_changements = int(input())


liste_positions =[""] * nb_positions

for i in range(nb_positions):
    liste_positions[i] = int(input())

for changement in range(nb_changements) :
    changement_1 = int(input())
    changement_2 = int(input())
    x = liste_positions[changement_1]
    liste_positions[changement_1] = liste_positions[changement_2]
    liste_positions[changement_2] = x

for position in range(nb_positions):  
    print(liste_positions[position])
