
#Exercice 4
t1=[100,28,31,1,31,30,31,31,30,31,30,31]
#a)Compter nombre éléments non nuls
compteur = 0
for i in range(len(t1)):
    if t1[i] != 0:
        compteur = compteur + 1
print(compteur)

#b)Le plus grand élément
max = max(t1)

#c)La position p du plus petit élément
plusPetit = min(t1)
p = 0
for i in range(len(t1)): 
    if t1[i] == plusPetit:
        p = i+1

#d)

#Exercice 5
#Créer à partir de la liste t1, une liste qui contienne seulement les nombres pairs
#et une qui contienne les nombres impairs
print("EXERCICE 5")
nbPairs=[]
nbImpairs=[]
for i in range(len(t1)):
    if (t1[i]%2)==0:
        nbPairs.append(t1[i])
    else:
        nbImpairs.append(t1[i])

#Exercice 3
print("EXERCICE 3")
for nombre in nbPairs:
    print(nombre,"", end="")

#Exercice 6
prenom = ["Jean", "Maximilien", "Brigitte", "Shiny", "Cedric", "Joanna", "Salope"]
moinsDe6carac = []
plusDe6carac =[]

for i in range(len(prenom)):
    if(len(prenom[i])) < 6:
        moinsDe6carac.append(prenom[i])
    else:
        plusDe6carac.append(prenom[i])
#Exercice 7
print("EXERCICE 7")
nombres=list(range(1,10))
print(nombres)
for i in range(1, len(nombres), 2):
    nombres[i] = nombres[i-1]
print(nombres)
for i in range(
