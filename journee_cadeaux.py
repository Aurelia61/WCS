nb_habitants = int(input())
fortune_habitant = [""] * nb_habitants

for habitant in range(nb_habitants):
    fortune_habitant[habitant] = int(input())

fortune_habitant.sort()

if nb_habitants % 2 == 0 :
    milieu = int(nb_habitants//2)
    milieu_inf = fortune_habitant[milieu-1]
    milieu_sup = fortune_habitant[milieu+1]
    milieu_ok = (milieu_sup-milieu_inf)//2 + milieu_inf
    valeur = fortune_habitant[milieu_ok]
    print(valeur)
else :
    milieu = (nb_habitants-1)//2
    valeur = fortune_habitant[milieu]
    print(valeur)