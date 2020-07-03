nb_habitants = int(input())
somme_fortune = 0


if nb_habitants % 2 != 0:

    for habitant in range( nb_habitants) :
        fortune = int(input())
        somme_fortune += fortune
    print(round(somme_fortune/nb_habitants))

else:
    for habitant in range( nb_habitants) :
        fortune = int(input())
        somme_fortune += fortune
    print(round(somme_fortune/nb_habitants+1,1))