nbOperations=int(input())
 
stock=[0]*10
 
for i in range(nbOperations):
    num=int(input())
    num=num-1
    qte=int(input())
    stock[num]=stock[num]+qte
print(*stock, sep='\n')