def lire_lignes(fichier):
    with open(fichier, 'r') as f:
        lignes = f.readlines()
    return [ligne.strip() for ligne in lignes]

lignes = lire_lignes("data/data5.txt")


partie = True
partie_1 = []
partie_2 = []
nouvelle_partie_2 = []
encore_nouvelle_partie_2_ENCORE = []

res = 0


for i, ligne in enumerate(lignes):
    if ligne.strip() == "":
        partie = False
        continue

    if partie:
        temp = ligne.split("|")
        partie_1.append([int(x) for x in temp])
    else:
        temp_2 = ligne.split(",")
        partie_2.append([int(x) for x in temp_2])


for i in partie_2:
    val = True
    #print(i)
    for j in partie_1:
        nb1, nb2 = j[0], j[1]
        if all(k in i for k in [nb1,nb2]):
            if i.index(nb1) > i.index(nb2):
                val = False
                break
    
    if val:
        nouvelle_partie_2.append(i)

partie_2 = [x for x in partie_2 if x not in nouvelle_partie_2]

for i in partie_2:
    echange = True
    while(echange):
        echange = False
        for j in partie_1:
            nb1, nb2 = j[0], j[1]
            if nb1 in i and nb2 in i:
                index1, index2 = i.index(nb1), i.index(nb2)
                if index1 > index2:
                        i[index1], i[index2]= i[index2], i[index1]
                        echange = True

    encore_nouvelle_partie_2_ENCORE.append(i)


for i in encore_nouvelle_partie_2_ENCORE:
    res += i[len(i) // 2]

print(res)