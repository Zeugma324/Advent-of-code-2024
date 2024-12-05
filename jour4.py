def lire_lignes(fichier):
    with open(fichier, 'r') as f:
        lignes = f.readlines()
    return [ligne.strip() for ligne in lignes]

res_1 = 0
res_2 = 0

lignes = lire_lignes("data/data4.txt")

for i, ligne in enumerate(lignes):
    prec1_ligne = lignes[i-1] if i > 0 else None
    prec2_ligne = lignes[i-2] if i > 1 else None
    prec3_ligne = lignes[i-3] if i > 2 else None

    sui1_ligne = lignes[i+1] if i < len(lignes) - 1 else None
    sui2_ligne = lignes[i+2] if i < len(lignes) - 2 else None
    sui3_ligne = lignes[i+3] if i < len(lignes) - 3 else None


    for j, c in enumerate(ligne):
        if c == "X":
            if ligne[j+1:j+4] == "MAS":
                res_1 += 1
            if j >= 3 and ligne[j-3:j] == "SAM":
                res_1 += 1
                
            if prec1_ligne and prec2_ligne and prec3_ligne:
                if prec1_ligne[j] == "M" and prec2_ligne[j] == "A" and prec3_ligne[j] == "S":
                    res_1 += 1
                if j >= 3 and prec1_ligne[j-1] == "M" and prec2_ligne[j-2] == "A" and prec3_ligne[j-3] == "S":
                    res_1 += 1
                if j < len(ligne) - 3 and prec1_ligne[j+1] == "M" and prec2_ligne[j+2] == "A" and prec3_ligne[j+3] == "S":
                    res_1 += 1
                    
            if sui1_ligne and sui2_ligne and sui3_ligne:
                if sui1_ligne[j] == "M" and sui2_ligne[j] == "A" and sui3_ligne[j] == "S":
                    res_1 += 1
                if j >= 3 and sui1_ligne[j-1] == "M" and sui2_ligne[j-2] == "A" and sui3_ligne[j-3] == "S":
                    res_1 += 1
                if j < len(ligne) - 3 and sui1_ligne[j+1] == "M" and sui2_ligne[j+2] == "A" and sui3_ligne[j+3] == "S":
                    res_1 += 1

print(res_1)

for i, ligne in enumerate(lignes):
    prec1_ligne = lignes[i-1] if i > 0 else None


    sui1_ligne = lignes[i+1] if i < len(lignes) - 1 else None


    for j, c in enumerate(ligne):
        if c == "A" and prec1_ligne and sui1_ligne:
            if 1 <= j < len(ligne) - 1:
                if prec1_ligne[j-1] == "M" and sui1_ligne[j+1] == "S" and prec1_ligne[j+1] == "S" and sui1_ligne[j-1] == "M":
                    res_2 += 1
                if prec1_ligne[j-1] == "M" and sui1_ligne[j+1] == "S" and prec1_ligne[j+1] == "M" and sui1_ligne[j-1] == "S":
                    res_2 += 1
                if prec1_ligne[j-1] == "S" and sui1_ligne[j+1] == "M" and prec1_ligne[j+1] == "S" and sui1_ligne[j-1] == "M":
                    res_2 += 1
                if prec1_ligne[j-1] == "S" and sui1_ligne[j+1] == "M" and prec1_ligne[j+1] == "M" and sui1_ligne[j-1] == "S":
                    res_2 += 1

print(res_2)