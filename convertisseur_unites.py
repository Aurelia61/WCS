nb_conversions = int(input())

for chiffre in range(nb_conversions) :
    conversion = input()
    conversion = list(conversion)
    if conversion[len(conversion)-1] == "m" :
        conversion = conversion[:len(conversion)-1]
        conversion =float("".join(conversion))
        conversion *= 3.28083992
        print("{} p".format(round(conversion,6)))
    elif conversion[len(conversion)-1] == "g" :
        conversion = conversion[:len(conversion)-1]
        conversion =float("".join(conversion))
        conversion *= 0.002205
        print("{} l".format(round(conversion,6)))
    elif conversion[len(conversion)-1] == "c" :
        conversion = conversion[:len(conversion)-1]
        conversion =float("".join(conversion))
        conversion = 32 + (1.8 * conversion)
        print("{} f".format(round(conversion,6)))


### solution france ioi :

# def mètresVersPieds(mètres):
#    return mètres / .3048
# def grammesVersLivres(grammes):
#    return grammes * .002205
# def celsiusVersFarenheit(celsius):
#    return 32 + celsius * 1.8
# nbValeurs = int(input())
# for loop in range(nbValeurs):
#    valeur, unité = input().split()
#    valeur = float(valeur)
#    if unité == 'm':
#       print(mètresVersPieds(valeur), 'p')
#    elif unité == 'g':
#       print(grammesVersLivres(valeur), 'l')
#    elif unité == 'c':
#       print(celsiusVersFarenheit(valeur), 'f')

