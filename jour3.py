import re

def lire_lignes(fichier):
    with open(fichier, 'r') as f:
        lignes = f.readlines()
    return [ligne.strip() for ligne in lignes]

res = 0
pattern = r"mul\(\d+,\d+\)"
pattern_2 = r"\d+"
pattern_do = r"do\(\)"
pattern_dont = r"don't\(\)"
pattern_bout = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"

oui = True

for i, ligne in enumerate(lire_lignes("data/data3.txt")):
    bouts = re.findall(pattern_bout, ligne)
    for bout in bouts:
        if bout == "do()":
            oui = True
        elif bout == "don't()":
            oui = False
        if oui:
            match_1 = re.findall(pattern, bout)
            for n in match_1:
                match_2 = re.findall(pattern_2, n)
                res += int(match_2[0]) * int(match_2[1])

print(res)