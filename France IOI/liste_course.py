prix = [9,5,12,15,7,42,13,10,1,20]
cout_total = 0
for ingredient in range(10):
    nb = int(input())
    cout_total += nb * prix[ingredient]

print(cout_total)