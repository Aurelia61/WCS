titre = input()
nom = input()

for lettre in range(len(titre)) :
    if titre[lettre] != "A" or titre[lettre] != "E" or titre[lettre] != "I" or titre[lettre] != "U" or titre[lettre] != "Y" :
        titre[lettre]= titre[lettre]
        print(titre[::])
for lettre in range(len(nom)) :
    if nom[lettre] != "A" or nom[lettre] != "E" or nom[lettre] != "I" or nom[lettre] != "U" or nom[lettre] != "Y" :
        print(nom[::])