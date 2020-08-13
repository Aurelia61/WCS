



liste = ["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"]
k = 2

# print(len(liste[0])+len(liste[1]))
lenght_max = 0
lenght = 0
for index in range(len(liste)-1):
    print(f'le mot à l index {index} :: {liste[index]}')
    print(f'longueur du mot {liste[index]} :: {len(liste[index])}')
    for number in range (k):
        lenght += len(liste[index+number])
        print(f'longueur {number} {liste[index+number]} :: {len(liste[index+number])}')
        if lenght > lenght_max :
            lenght_max = lenght
            print(f'longueur max :: {lenght_max}')
            concatener = liste[index]+liste[index+1]
            print(f'résultat concaténé :: {concatener}')
        


# liste = ["maison", "at"]
# print(len(liste))
# for word in liste :
#     print(f'le mot :: {word}')
#     print(len(word))
# print(f'le mot à l indice 0 :: {liste[0]}')
# print(f'la longueur du mot a l indice 0 :: {len(liste[0])}')