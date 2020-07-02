nb_deplacements = int(input())
deplacements = [""]*nb_deplacements

for num in range(nb_deplacements) :
    deplacements[num] = int(input())

for num in range(nb_deplacements):
    if deplacements[num] == 1 :
        deplacements[num] = 2
    elif  deplacements[num] == 4 :
        deplacements[num] = 5

for num in range(0,nb_deplacements, -1):
    print(deplacements[num])

