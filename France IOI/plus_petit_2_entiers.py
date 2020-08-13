
def min2(nb_1, nb_2) :
    if nb_1 < nb_2 :
        return nb_1
    else:
        return nb_2

nb_min = int(input())
for nombre in range(9) :
    nb_min = min2(nb_min, int(input()))

print(nb_min)