nb_participants = int(input())
nombres_participants = [""] * nb_participants

for participant in range(nb_participants) :
    nombres_participants[participant] = int(input())

nombres_participants.sort()

print(nombres_participants)

# for i in (nb_participants/2) :
print("{} {}".format(nb_participants[0], nb_participants[nb_participants]))

