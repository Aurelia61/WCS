nb_mesures = int(input())
little = int(input())
bigger = int(input())
flag = True
for mesure in range(nb_mesures):
    x  = int(input())
    if x >= little and x <= bigger and flag:
        print("Rien à signaler")
    if (x < little or x > bigger) and flag:
        print("Alerte !!")
        flag = False