code_bon = 4242

def demander_le_code() :
    code = 0
    while code != code_bon :
        print("Entrez le code :")
        code = int(input())

demander_le_code()
print("Encore une fois.")
demander_le_code()
print("Bravo.")