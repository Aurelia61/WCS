from math import sqrt 

def comp(array1, array2) :
    for number in array2 :
        print(f' racine carré de {array2}  :: {int(sqrt(array2))}')


comp(121,[121, 14641, 20736, 361, 25921])