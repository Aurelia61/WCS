for nb in range(10) :
    print(nb)


# BREAK

print()
print()
for nb in range(10):
    if nb > 7 :
        break   # arrete la boucle
    print(nb)


# CONTINUE

print()
print()
for nb in range(10):
    if nb % 2 == 0: # saute les nombres paires
        continue
    if nb > 7 :
        break
    print(nb)