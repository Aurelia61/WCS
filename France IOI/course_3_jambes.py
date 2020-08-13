nb_participants = int(input())
nombres_participants = [""] * nb_participants

for participant in range(nb_participants) :
    nombres_participants[participant] = int(input())

nombres_participants.sort()

valeur_max = nb_participants-1


for i in range(nb_participants // 2) :
    print("{} {}".format(nombres_participants[i],nombres_participants[valeur_max]))
    valeur_max-=1
