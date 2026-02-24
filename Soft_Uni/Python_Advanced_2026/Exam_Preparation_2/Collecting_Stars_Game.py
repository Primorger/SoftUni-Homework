n = int(input())

matrix = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "P":
            player_r = row
            player_c = col

stars_collected = 2 

matrix[player_r][player_c] = "."

directions = {
    "up":    (-1, 0),
    "down":  (1, 0),
    "left":  (0, -1),
    "right": (0, 1)
}

while True:
    direction = input()
    move = directions[direction]
    row = player_r + move[0]
    col = player_c + move[1]

    if 0 > row or row > n - 1 or 0 > col or col > n - 1:
        player_r, player_c = 0, 0
        if matrix[player_r][player_c] == "*":
            stars_collected += 1
            matrix[player_r][player_c] = "."
            if stars_collected == 10:
                break

    elif matrix[row][col] == "#":
        stars_collected -= 1
        if stars_collected == 0:
            break

    else:
        player_r, player_c = row, col
        
        if matrix[row][col] == "*":
            stars_collected += 1
            matrix[row][col] = "."
            
            if stars_collected == 10:
                break

matrix[player_r][player_c] = "P"

if stars_collected == 10:
    print("You won! You have collected 10 stars.")
elif stars_collected == 0:
    print("Game over! You are out of any stars.")

print(f"Your final position is [{player_r}, {player_c}]")

for line in matrix:
    print(*line)