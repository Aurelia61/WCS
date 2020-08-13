nb_livres = int(input())
longueur_minimale = int(input())

for livre in range (nb_livres):
    titre = input()
    resume = input()

if len(resume) < longueur_minimale :
    print(titre)