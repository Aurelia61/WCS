nbPersonnes = int(input())
fortune = [0] * nbPersonnes
for idPersonne in range(nbPersonnes):
   fortune[idPersonne] = int(input())
fortune.sort()
if nbPersonnes % 2 == 1:
   milieu = (nbPersonnes - 1) // 2
   print( fortune[milieu] )
else:
   milieu = nbPersonnes // 2
   print( ( fortune[milieu - 1] + fortune[milieu] ) / 2 )
