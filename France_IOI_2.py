from math import *

pop_actuelle = int(input())
croissance = float(input())

nouvelle_population = pop_actuelle + pop_actuelle * croissance / 100
print (floor(nouvelle_population))