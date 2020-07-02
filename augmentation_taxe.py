taxe_actuelle = float(input())
nouvelle_taxe = float(input())
prix_ttc = float(input())

nouveau_prix = ((prix_ttc) / (taxe_actuelle/100+1)) * (nouvelle_taxe/100+1)*100

print(round(nouveau_prix)/100)

prixFutur=(round(((prix_ttc/(1+taxe_actuelle/100))*(1+nouvelle_taxe/100))*100))/100
print(prixFutur)