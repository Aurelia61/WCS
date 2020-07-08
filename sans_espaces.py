
texte = input()

liste = list(texte)

for caractere in range( len(liste)) :
    if liste[caractere] == " " :
        liste[caractere] = "_"

texte = "".join(liste)

print(texte)


### DEUX solutions France ioi ::
# texte = list(input())
# for pos in range(len(texte)):
#     if texte[pos] == " ":
#         texte[pos] = "_"
# print("".join(texte))

## sans modification du texte ::
# texte = input()
# for pos in range(len(texte)):
#     if texte[pos] == " ":
#         print("_", end = "")
#     else:
#         print(texte[pos], end = "")
# print()