import os
from functools import reduce

def lire_lignes(fichier):
    with open(fichier, 'r') as f:
        lignes = f.readlines()
    return [ligne.strip() for ligne in lignes]
    
lignes = lire_lignes("./advent of code 2024/data/datatest.txt")


res_temp = 1
res = 0

boites = {}

def gethash(a):
    value = 0
    for k in a:
        value = ((value + ord(k)) * 17)%256
    return value    

for i, ligne in enumerate(lignes):
    tab = ligne.split(",")
    for j in tab:
        if "=" in j:
            bout = j.split("=")
            focal = int(bout[1])
            hash = gethash(bout[0])

            if hash not in boites:
                boites[hash] = []

            trouvé = False
            for index, item in enumerate(boites[hash]):
                if item[0] == bout[0]:
                    boites[hash][index] = (bout[0], focal)
                    trouvé = True
                    break
            if not trouvé:
                boites[hash].append((bout[0], focal))
        elif "-" in j:
            bout = j.split("-")
            hash = gethash(bout[0])
            if hash in boites:
                boites[hash] = [item for item in boites[hash] if item[0] != bout[0]]


for i in boites:
    res_temp = 0
    for j, item in enumerate(boites[i]):
        temptemp = (j+1)*item[1]
        res_temp += temptemp
    res_temp *= (i + 1)
    res += res_temp


        
print(res)
