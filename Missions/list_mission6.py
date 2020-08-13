liste_1 = ["a", "b", "c", "d"]
liste_2 = ["b", "d", "e", "f"]
liste_3 = ["a", "f", "g", "h"]
egalite_1_2 = 0
egalite_1_3 = 0
egalite_2_3 = 0


for element in range(len(liste_1)) :
    for element_2 in range(len(liste_2)):
        if liste_1[element] == liste_2[element_2] :
            egalite_1_2 += 1

for element in range(len(liste_1)) :
    for element_2 in range(len(liste_3)):
        if liste_1[element] == liste_3[element_2] :
            egalite_1_3 += 1

for element in range(len(liste_2)) :
    for element_2 in range(len(liste_3)):
        if liste_2[element] == liste_3[element_2] :
            egalite_2_3 += 1

if egalite_1_2 > egalite_1_3 :
    print("1 et 2 sont proches.")
elif egalite_1_2 > egalite_2_3 :
    print("1 et 2 sont proches.")
elif egalite_1_3 > egalite_2_3 :
    print("1 et 3 sont proches.")
elif egalite_1_3 > egalite_1_2 :
    print("1 et 3 sont proches.")
elif egalite_2_3 > egalite_1_2 :
    print("2 et 3 sont proches.")
elif egalite_2_3 > egalite_1_3 :
    print("2 et 3 sont proches.")

