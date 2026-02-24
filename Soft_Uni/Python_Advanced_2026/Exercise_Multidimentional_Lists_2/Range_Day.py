SIZE = 5

matrix = []
my_pos = []
targets = 0

for row in range(SIZE):
    matrix.append(input().split())
    for col in range(SIZE):
        if matrix[row][col] == "A":
            my_pos = [row, col]
        elif matrix[row][col] == "x":
            targets +=1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0 ,1)
}

targets_pos = []

for _ in range(int(input())):
    command = input().split()

    action = command[0]
    direction = command[1]

    if action == "shoot":

        row = my_pos[0] + directions[direction][0]
        col = my_pos[1] + directions[direction][1]
    
        while 0 <= row < SIZE and 0 <= col < SIZE:
            if matrix[row][col] == "x":
                targets_pos.append([row, col])
                matrix[row][col] = "."
                targets -= 1
                break

            row += directions[direction][0]
            col += directions[direction][1]

        if targets == 0:
            print(f"Training completed! All {len(targets_pos)} targets hit.")
            break

    elif action == "move":
        steps = int(command[2])

        row = my_pos[0] + directions[direction][0] * steps
        col = my_pos[1] + directions[direction][1] * steps

        if 0 <= row < SIZE and 0 <= col < SIZE and matrix[row][col] == ".":

            matrix[my_pos[0]][my_pos[1]] == "."
            matrix[row][col] = "A"
            my_pos = [row, col]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")

[print(target) for target in targets_pos]