nb_operations = int(input())
quantite_ingredients =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 11 emplacements alors que 10 ingredients !
# car c'est plus logique que le numéro du premier ingredient commence à 1.
# donc la valeur dans l'indice [0] de quantite_ingredient n'est pas utilisé.

for value in range(nb_operations) :
    num_ingredient = int(input())
    quantite =int(input())
    quantite_ingredients[num_ingredient] += quantite


for num_ingredient in range(1, 11) :
    print(quantite_ingredients[num_ingredient])