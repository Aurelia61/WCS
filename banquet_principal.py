nbPositions = int(input())
nbChangements = int(input())
 
tableau = [0] * (nbPositions)
 
for position in range(0 , nbPositions) :
    place = int(input())
    tableau[position] = place
    
     
for loop in range(nbChangements) :
    changement1 = int(input())
    changement2 = int(input())
    changementtmp = changement1
    
    tableau[changement1] = tableau[changement2]
    tableau[changement2] = changementtmp
    
    
 
for position in range(0, nbPositions):  
    print()
    print(tableau[position], " ")
