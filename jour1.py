def lire_lignes(fichier):
    with open(fichier, 'r') as f:
        lignes = f.readlines()
    return [ligne.strip() for ligne in lignes]

liste_1 = []
liste_2 = []

res_1 = 0
res_2 = 0

for i, ligne in enumerate(lire_lignes("./advent of code 2024/data/data1.txt")):
    a, b =ligne.split()
    liste_1.append(int(a))
    liste_2.append(int(b))

for i in liste_1:
    res_2 += i * liste_2.count(i)

while liste_1:
    res_1 += max(min(liste_1),min(liste_2)) - min(min(liste_1),min(liste_2))
    liste_1.remove(min(liste_1))
    liste_2.remove(min(liste_2))
    

print(res_1)
print(res_2)