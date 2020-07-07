# !! Le nom de la clé est immuable.
# pour la changer, il faut la supprimer avec pop pour récupérer les valeurs

MyDict = {
    "Javier" : 45,
    ("Aurélia", "Thomas") : 38,  # !! clé composée :: difficile à utiliser car il faut appeler la clé avec le tuple en entier (ici, prénom + nom)
    "Alex" : None,
    "Laura" : True
}

for MyKey, MyValue in MyDict.items():
    print(f"{MyKey} a {MyValue} ans")

for MyKey in MyDict.keys() :
    print(f"{MyKey}")

for MyValue in MyDict.values() :
    print(f"{MyValue}")


MyDict["Mélanie"] = None
print (MyDict)


# .pop est une méthode
print(MyDict.pop("Alex"))     # on enlève la valeur et on récupère les valeurs

# del est une fonction
del MyDict["Laura"]
print(MyDict)