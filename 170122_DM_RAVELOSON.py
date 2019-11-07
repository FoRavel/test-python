#RAVELOSON Fanilo

listeMontant = []
montant = 0

while montant != -1:
    montant = int(input("Entrez le montant de la vente: "))
    print(montant)
    listeMontant.append(montant)

listeMontant.remove(-1)
print("Montant des ventes de la journée: " , listeMontant, " euros")

print("Montant total: ", sum(listeMontant), " euros")
print("Montant minimal: ", min(listeMontant), " euros")
print("Montant maximal: ", max(listeMontant), " euros")
moyenneListe = sum(listeMontant)/len(listeMontant)
print("Moyenne des ventes: ", moyenneListe, " euros")

n = 0

for i in range(len(listeMontant)):
    if listeMontant[i]<moyenneListe:
        n=n+1
print(n, " ventes sont inférieurs à la moyenne")
