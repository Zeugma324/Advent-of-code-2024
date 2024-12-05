def lire_lignes(fichier):
    with open(fichier, 'r') as f:
        lignes = f.readlines()
    return [ligne.strip() for ligne in lignes]

def bon_niveau(niveau):
    if niveau == sorted(niveau):
        if all(1 <= abs(niveau[i] - niveau[i+1]) <= 3 for i in range(len(niveau) - 1)):
            return True
    elif niveau == sorted(niveau, reverse=True):
        if all(1 <= abs(niveau[i] - niveau[i+1]) <= 3 for i in range(len(niveau) - 1)):
            return True
    else:
        return False

niveau = []
res = 0

for i, ligne in enumerate(lire_lignes("data/data2.txt")):
    niveau = []

    for d in ligne.split():
        niveau.append(int(d))
    if bon_niveau(niveau):
        res += 1
    else :
        for j, niv in enumerate(niveau):
            niveau.pop(j)
            if bon_niveau(niveau):
                res += 1
                break
            niveau.insert(j,niv)

print(res)