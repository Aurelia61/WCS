#coding : utf-8

invent = { 'pommes' : 430, 'bananes' : 312, 'oranges' : 274, 'poires' : 137 }

print()
print (invent)
print()

del invent['pommes']
print (invent)
print()

print(invent.keys())
print()

print(f'les valeurs sont :: {invent.values()}')
print()

print(invent.items())
print()

for key, value in invent.items() :
    print ("Clé : %s, valeur : %s." % (key, value))
    print(f'Clé : {key}, valeur : {value}.')

print()

stock = {'raisins' : 12, 'citrons' : 132, 'poires' : 4}
print(invent)
invent.update(stock)
print(invent)
print(stock)