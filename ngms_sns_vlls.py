
# nom = input()

for loop in range(2) :  
    titre = input()
    for lettre in range(len(titre)) :
        if titre[lettre] != "A" and titre[lettre] != "E" and titre[lettre] != "I" and titre[lettre] != "U" and titre[lettre] != "Y" and titre[lettre] != " " :
            print(titre[lettre], end="")
    print()
# for lettre in range(len(nom)) :
#     if nom[lettre] != "A" and nom[lettre] != "E" and nom[lettre] != "I" and nom[lettre] != "U" and nom[lettre] != "Y" :
#         print(nom[::])