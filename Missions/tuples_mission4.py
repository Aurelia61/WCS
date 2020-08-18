integer_1 = (6,9,12)
integer_2 = (140,5,6)

def compare(nb_1, nb_2) :
    sum_nb_1 = sum(nb_1)
    sum_nb_2 = sum(nb_2)
    if sum_nb_1 > sum_nb_2 :
        return nb_1
    else :
        return nb_2

print(compare(integer_1, integer_2))