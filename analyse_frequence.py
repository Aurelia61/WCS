nb_lignes , nb_mots = input().split()
nb_trouve = [0] * int(nb_mots)
phrase_1 = input().split()
phrase_2 = input().split()


for mots in range(int(nb_mots)):
    if len(phrase_1[mots]) == 1 :
        nb_trouve[mots] += 1
for mots in range(int(nb_mots)):
    if len(phrase_2[mots]) == 1 :
        nb_trouve[mots] += 1
for mots in range(int(nb_mots)):
    if len(phrase_1[mots]) == 2 :
        nb_trouve[mots] += 1
for mots in range(int(nb_mots)):
    if len(phrase_2[mots]) == 2 :
        nb_trouve[mots] += 1
for mots in range(int(nb_mots)):
    if len(phrase_1[mots]) == 3 :
        nb_trouve[mots] += 1
for mots in range(int(nb_mots)):
    if len(phrase_2[mots]) == 3 :
        nb_trouve[mots] += 1
for mots in range(int(nb_mots)):
    if len(phrase_1[mots]) == 4 :
        nb_trouve[mots] += 1
for mots in range(int(nb_mots)):
    if len(phrase_2[mots]) == 4 :
        nb_trouve[mots] += 1
for mots in range(int(nb_mots)):
    if len(phrase_1[mots]) == 5 :
        nb_trouve[mots] += 1
for mots in range(int(nb_mots)):
    if len(phrase_2[mots]) == 5 :
        nb_trouve[mots] += 1
for mots in range(int(nb_mots)):
    if len(phrase_1[mots]) == 6 :
        nb_trouve[mots] += 1
for mots in range(int(nb_mots)):
    if len(phrase_2[mots]) == 6 :
        nb_trouve[mots] += 1
for mots in range(int(nb_mots)):
    if len(phrase_1[mots]) == 7 :
        nb_trouve[mots] += 1
for mots in range(int(nb_mots)):
    if len(phrase_2[mots]) == 7 :
        nb_trouve[mots] += 1

print("{} {} {}".format(mots, " : ", nb_trouve[mots]))