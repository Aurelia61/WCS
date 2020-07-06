nom = input()
if nom[0] <= "F" and nom[0] >= "A":
    print('1')
if nom[0] >= "G" and nom[0] <= "P" :
    print("2")
if nom[0] > "P" :
    print("3")

## solution simplifiée 
# nom = input()
# if nom[0] <= "F":
#    print(1)
# elif nom[0] <= "P":
#    print(2)
# else:
#    print(3)