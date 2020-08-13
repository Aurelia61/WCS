nombre = int(input())

def calcul(nombre):
    while nombre != 1 :
        if nombre %2 == 0 :
            nombre = nombre//2
            print(nombre, end=" ")
            
        else :
            nombre = nombre*3+1
            print(nombre, end=" ")

calcul(nombre)

### solution france ioi ::
# def termeSuivant(terme):
#     if terme % 2 == 0:
#       return terme // 2
#     else:
#         return terme * 3 + 1
# terme = int(input())
# while terme != 1:
#     terme = termeSuivant(terme)
#     print(terme, end = " ")
# print()