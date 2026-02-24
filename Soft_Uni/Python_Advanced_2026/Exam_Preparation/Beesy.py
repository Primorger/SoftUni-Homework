NECTAR_NEEDED = 30

field_size = int(input())

field = []

energy = 15
energy_restored = False
nectar_collected = 0

for row in range(field_size):
    field.append(list(input()))
    for col in range(field_size):
        if field[row][col] == "B":
            bee_pos = [row, col]
            field[row][col] = "-"

def move_bee(dir, coords):
    r, c = coords

    if dir == "up":
        r = (r - 1) % field_size
    elif dir == "down":
        r = (r + 1) % field_size
    elif dir == "left":
        c = (c - 1) % field_size
    elif dir == "right":
        c = (c + 1) % field_size
    return r, c

while True:
    energy -= 1
    bee_pos = move_bee(input(), bee_pos)

    if field[bee_pos[0]][bee_pos[1]].isdigit():
        nectar_collected += int(field[bee_pos[0]][bee_pos[1]])
        field[bee_pos[0]][bee_pos[1]] = "-"

    if field[bee_pos[0]][bee_pos[1]] == "H":
        if nectar_collected >= NECTAR_NEEDED:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print(f"Beesy did not manage to collect enough nectar.")
        break

    if energy <= 0:
        if not energy_restored and nectar_collected >= NECTAR_NEEDED:
            energy = nectar_collected - NECTAR_NEEDED
            energy_restored = True
            nectar_collected = NECTAR_NEEDED
        else:
            print("This is the end! Beesy ran out of energy.")
            break

field[bee_pos[0]][bee_pos[1]] = "B"

[print(*row, sep="") for row in field]