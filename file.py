nb_total_mesures = int(input())
temp_min = int(input())
temp_max = int(input())
nb_mesures = 0

if nb_mesures < nb_total_mesures :
    temp_mesuree = int(input())
    while (temp_mesuree < temp_max 
        or temp_mesuree > temp_min 
        and nb_mesures+1 != nb_total_mesures) :
        print("Rien à signaler")
        nb_mesures += 1
   
    print("Alerte !!")
    
    