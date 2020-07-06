
nb_positions = int(input())
nb_changements = int(input())


positions_initiales =[""] * nb_positions

for i in range(nb_positions):
    positions_initiales[i] = int(input())

for changement in range(nb_changements) :
    changement_1 = int(input())
    changement_2 = int(input())
    changement = changement_1+1
    positions_initiales[changement_1-1] = changement_2+1
    positions_initiales[changement_2-1] = changement

print(positions_initiales)

