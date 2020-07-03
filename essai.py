nb_habitants = int(input())
fortune_habitant = [""] * nb_habitants

for habitant in range(nb_habitants):
    fortune_habitant[habitant] = int(input())

fortune_habitant.sort()

if nb_habitants % 2 == 0 :
    milieu = nb_habitants//2
    valeur = fortune_habitant[milieu]
else :
    milieu = (nb_habitants-1)//2 
    valeur = fortune_habitant[milieu]


print(valeur)
