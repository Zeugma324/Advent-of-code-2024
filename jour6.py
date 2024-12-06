def lire_lignes(fichier):
    with open(fichier, 'r') as f:
        return [list(l.strip()) for l in f.readlines()]

grid = lire_lignes("data/data6.txt")
rows, cols = len(grid), len(grid[0])
base_x = 0
base_y = 0
boucle = 0

for i, ligne in enumerate(grid):
    for j, char in enumerate(ligne):
        if char == "^":
            base_x, base_y = i, j
            break

def findpath(x, y, grid):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dir_symbols = ['^', '>', 'v', '<']

    d = dir_symbols.index(grid[x][y])
    visited = set()
    visited.add((x,y,d))

    while True:
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
            break

        if grid[nx][ny] == '#':
            d = (d + 1) % 4
        else:
            x, y = nx, ny
            if (nx, ny, d) in visited:
                return True
            visited.add((x, y, d))

        
    return False


for i, ligne in enumerate(grid):
    for j, char in enumerate(ligne):
        if (i, j) != (base_x, base_y) and char == ".":
            origin_char = ligne[j]
            ligne[j] = "#"
            if findpath(base_x, base_y, grid):
                boucle += 1
            ligne[j] = origin_char
        

print(boucle)