def find_it(seq):
    for letter in set(seq) :
        nb_letter = seq.count(letter)
        if nb_letter % 2 != 0 :
            return letter


print(find_it([5,4,3,2,1,5,4,3,2,10,10]))

# solution plus courte ::
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i