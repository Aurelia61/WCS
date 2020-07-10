import random
liste = ["a", "b", "c", "d"]
liste.insert(random.randint(0,len(liste)-1), "e")

print(liste)