taxe_actuelle = float(input())
nouvelle_taxe = float(input())
prix_ttc = float(input())

prix_ht = round(prix_ttc) / (5/100+1)

nouveau_prix = round(prix_ht) * nouvelle_taxe(100+1)*100

print(round(nouveau_prix))