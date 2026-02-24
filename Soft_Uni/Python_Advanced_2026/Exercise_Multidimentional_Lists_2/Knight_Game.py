n = int(input())

matrix = []
knights = []

for row in range(n):
    matrix.append(list(input()))
    for col in range(n):
        if matrix[row][col] == 'K':
            knights.append([row, col])

def count_attacks(r, c):
    attacks = 0
    moves = [
        (-2, -1), (-2, +1), (+2, -1), (+2, +1),
        (-1, -2), (-1, +2), (+1, -2), (+1, +2)
    ]

    for row, col in moves:
        new_row, new_col = r + row, c + col

        if 0 <= new_row < n and 0 <= new_col < n:
            
            if matrix[new_row][new_col] == 'K':
                attacks += 1
    return attacks

removed_knights = 0

while True:
    max_attacks = 0
    knight_to_remove = None

    for r, c in knights:
        attacks = count_attacks(r, c)

        if attacks > max_attacks:
            max_attacks = attacks
            knight_to_remove = (r, c)

    if max_attacks == 0:
        break

    r, c = knight_to_remove
    matrix[r][c] = '0'
    
    knights.remove([r, c])
    removed_knights += 1

print(removed_knights)