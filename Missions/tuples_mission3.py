my_tuple = (
    9, 
    6, 
    12,
    "Hello World !", 
    "Python", 
    "Bravo !",
    ["bleu", "rouge", "vert"], 
    ["marron", "orange", "kaki"], 
    {"name" : "Aurélia", "adresse" : "L Aigle", "numéro" : "61"}, 
    {"pierre" : 1, "feuille" : 2, "cisceaux" : 3}
)


my_tuple = my_tuple[0:3] + ("Bonjour",) + my_tuple[4:]

print(my_tuple)