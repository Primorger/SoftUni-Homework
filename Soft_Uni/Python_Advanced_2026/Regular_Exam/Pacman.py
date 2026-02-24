N = int(input())

matrix = []

stars = 0
stars_collected = 0
health = 100
freezed = False

for row in range(N):
    matrix.append(list(input()))
    for col in range(N):
        if matrix[row][col] == "P":
            pacman_r = row
            pacman_c = col
        if matrix[row][col] == "*":
            stars += 1

matrix[pacman_r][pacman_c] = "-"

directions = {
    "up":    (-1, 0),
    "down":  (1, 0),
    "left":  (0, -1),
    "right": (0, 1)
}

def move_bee(dir, coords):
    r, c = coords

    if dir == "up":
        r = (r - 1) % N
    elif dir == "down":
        r = (r + 1) % N
    elif dir == "left":
        c = (c - 1) % N
    elif dir == "right":
        c = (c + 1) % N

    return r, c

while True:
    command = input()

    if command == "end":
        break
    if stars_collected == stars:
        break
    if health == 0:
        break

    pacman_r, pacman_c = move_bee(command, [pacman_r, pacman_c])

    if matrix[pacman_r][pacman_c] == "*":
        matrix[pacman_r][pacman_c] = "-"
        stars_collected += 1
        freezed = False

    elif matrix[pacman_r][pacman_c] == "-":
        freezed = False

    elif matrix[pacman_r][pacman_c] == "G":
        matrix[pacman_r][pacman_c] = "-"
        if not freezed:
            health -= 50
        freezed = False

    elif matrix[pacman_r][pacman_c] == "F":
        matrix[pacman_r][pacman_c] = "-"
        freezed = True
    
matrix[pacman_r][pacman_c] = "P"

if health == 0:
    print(f"Game over! Pacman last coordinates [{pacman_r},{pacman_c}]")
elif stars_collected == stars:
    print(f"Pacman wins! All the stars are collected.")
elif command == "end":
    print(f"Pacman failed to collect all the stars.")

print(f"Health: {health}")

if stars_collected < stars:
    print(f"Uncollected stars: {stars - stars_collected}")

[print(*line, sep="") for line in matrix]