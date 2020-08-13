a = 13
print("A = " + str(a))

a +=5
b = int(input("Entrer un nombre : "))
a += b *2

print("A = " + str(a))

def increment(d1, max_range=2):
    for c in range(1,max_range):
        d1 += c
        print("A = " + str(d1))
    return d1

a = increment(a, max_range=5)

while a>10:
    a = a // 2
    if a %2 == 0:
        print ("A est pair("+str(a)+")")
    else:
        print("A est impair("+str(a)+")")

a = increment(a)

