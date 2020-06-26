from math import *

quantite_ciment = float(input())

kilo_sac = 60
nb_sacs = 0

while quantite_ciment > 0 :
    quantite_ciment = quantite_ciment - kilo_sac
    nb_sacs += 1

print(nb_sacs*45)


from math import *
 
quantiteCiment = float(input())
nbSacs = ceil(quantiteCiment / 60)
prix = nbSacs * 45
print(prix)