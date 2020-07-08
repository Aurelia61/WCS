lettre = input()

def uppercase(lettre) :
    if lettre == "a" or lettre == "e" or lettre == "i" or lettre == "o" or lettre == "u" or lettre == "y" :
        print(lettre.upper())
    else:
        print(lettre.lower())

uppercase(lettre)